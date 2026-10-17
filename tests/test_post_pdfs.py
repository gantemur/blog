"""Exercise preservation and failure boundaries using isolated synthetic posts."""
import hashlib
import json
import os
import shutil
import struct
import subprocess
import sys
import tempfile
import unittest
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
from post_pdf_provenance import source_record


def png(path):
    def chunk(kind, data):
        return struct.pack('>I', len(data)) + kind + data + struct.pack('>I', zlib.crc32(kind + data))
    pixels = b''.join(b'\0' + bytes([30, 100, 180]) * 64 for _ in range(32))
    path.write_bytes(b'\x89PNG\r\n\x1a\n' + chunk(b'IHDR', struct.pack('>IIBBBBB', 64, 32, 8, 2, 0, 0, 0)) + chunk(b'IDAT', zlib.compress(pixels)) + chunk(b'IEND', b''))


class PDFTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='blog-pdf-test-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        shutil.copytree(ROOT / 'scripts', self.root / 'scripts', ignore=shutil.ignore_patterns('__pycache__'))
        (self.root / 'src/posts').mkdir(parents=True)
        (self.root / 'src/assets').mkdir()
        (self.root / 'src/_data').mkdir()
        self.mapping = self.root / 'src/_data/post_pdfs.json'
        self.provenance = self.root / 'src/_data/post_pdf_provenance.json'
        mapping = {}; provenance = {}
        for slug in ['old-one', 'old-two']:
            post = self.post(slug)
            pdf = self.root / f'src/assets/pdf/posts/2000/01/01/{slug}.pdf'
            pdf.parent.mkdir(parents=True, exist_ok=True); pdf.write_bytes(b'%PDF-existing-' + slug.encode())
            mapping[f'/2000/01/01/{slug}/'] = f'/blog/assets/pdf/posts/2000/01/01/{slug}.pdf'
            provenance[f'/2000/01/01/{slug}/'] = source_record(self.root, post, pdf, {'test': 'sentinel'})
        self.mapping.write_text(json.dumps(mapping)); self.provenance.write_text(json.dumps(provenance))
        self.before = self.snapshot()
        self.bin = self.root / 'bin'; self.bin.mkdir()
        fake = self.bin / 'pandoc'
        fake.write_text('#!' + sys.executable + '\n' + '''import pathlib,sys
if '--version' in sys.argv:
 print('pandoc synthetic-test'); sys.exit(0)
source=pathlib.Path(sys.argv[1]).read_text()
if 'FAIL_RENDER' in source: sys.exit(2)
if 'MISSING_GLYPH' in source: print('Missing character: synthetic', file=sys.stderr)
pathlib.Path(sys.argv[sys.argv.index('-o')+1]).write_bytes(b'%PDF-test-render')
''')
        fake.chmod(0o755)
        engine = self.bin / 'xelatex'; engine.write_text('#!/bin/sh\nexit 0\n'); engine.chmod(0o755)

    def post(self, slug, body='Synthetic only.', pdf='true', permalink=None):
        p = self.root / f'src/posts/{slug}.md'
        p.write_text(f'---\ntitle: "Монгол туршилт"\ndate: "2000-01-01"\nslug: "{slug}"\npermalink: "{permalink or "/2000/01/01/"+slug+"/"}"\npdf: {pdf}\n---\n\n{body}\n')
        return p

    def snapshot(self):
        return {str(p.relative_to(self.root)): p.read_bytes() for p in (self.root / 'src').rglob('*') if p.is_file() and (p.suffix == '.pdf' or p.parent.name == '_data')}

    def run_script(self, script, *args, real=False):
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        if not real: env['PATH'] = str(self.bin) + os.pathsep + env.get('PATH', '')
        return subprocess.run([sys.executable, str(self.root / 'scripts' / script), *args], cwd=self.root, env=env, capture_output=True, text=True)

    def generate(self, slug, **kwargs):
        return self.run_script('export-post-pdfs.py', '--post', f'src/posts/{slug}.md', '--mainfont', 'DejaVu Serif', **kwargs)

    def test_targeted_generation_preserves_other_pdfs_and_mappings(self):
        self.post('new'); result = self.generate('new'); self.assertEqual(result.returncode, 0, result.stderr)
        after = self.snapshot()
        for path, data in self.before.items():
            if path.endswith('.pdf'): self.assertEqual(after[path], data)
        for path in [self.mapping, self.provenance]:
            old = json.loads(self.before[str(path.relative_to(self.root))]); new = json.loads(path.read_text())
            for key, value in old.items(): self.assertEqual(new[key], value)
        self.assertEqual(self.run_script('check-post-pdfs.py').returncode, 0)

    def test_failed_second_render_keeps_all_existing_outputs(self):
        self.post('new'); self.post('bad', 'FAIL_RENDER')
        result = self.run_script('export-post-pdfs.py', '--post', 'src/posts/new.md', '--post', 'src/posts/bad.md')
        self.assertNotEqual(result.returncode, 0); self.assertIn('Pandoc failed for', result.stderr); self.assertIn('bad.md', result.stderr); self.assertEqual(self.snapshot(), self.before)

    def test_missing_glyph_aborts_without_replacement(self):
        self.post('old-one', 'MISSING_GLYPH')
        result = self.generate('old-one')
        self.assertNotEqual(result.returncode, 0); self.assertIn('missing required glyphs', result.stderr)
        self.assertEqual(self.snapshot(), self.before)

    def test_static_and_external_overrides_are_never_regenerated(self):
        for name, value in [('remote', '\n  url: "https://example.com/paper.pdf"'), ('static', '\n  url: "/assets/custom.pdf"'), ('off', 'false')]:
            self.post(name, pdf=value)
            self.assertNotEqual(self.generate(name).returncode, 0)
            self.assertEqual(self.snapshot(), self.before)
        (self.root / 'src/assets/custom.pdf').write_bytes(b'%PDF-static')
        result = self.run_script('check-post-pdfs.py')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_source_change_fails_even_with_identical_mtime(self):
        p = self.root / 'src/posts/old-one.md'; stamp = p.stat().st_mtime_ns
        p.write_text(p.read_text() + '\nNew text.\n'); os.utime(p, ns=(stamp, stamp))
        result = self.run_script('check-post-pdfs.py')
        self.assertNotEqual(result.returncode, 0); self.assertIn('source changed', result.stdout)

    def test_asset_change_fails(self):
        image = self.root / 'src/assets/test.png'; png(image)
        self.post('new', '![Image](/blog/assets/test.png)')
        self.assertEqual(self.generate('new').returncode, 0)
        image.write_bytes(image.read_bytes() + b'changed')
        result = self.run_script('check-post-pdfs.py')
        self.assertNotEqual(result.returncode, 0); self.assertIn('image assets changed', result.stdout)

    def test_tampered_pdf_fails(self):
        p = next((self.root / 'src/assets/pdf').rglob('*.pdf')); p.write_bytes(b'changed')
        self.assertNotEqual(self.run_script('check-post-pdfs.py').returncode, 0)

    def test_no_selection_and_outside_paths_fail_without_changes(self):
        self.assertNotEqual(self.run_script('export-post-pdfs.py').returncode, 0)
        self.assertNotEqual(self.run_script('export-post-pdfs.py', '--post', '../outside.md').returncode, 0)
        self.assertEqual(self.snapshot(), self.before)

    def test_duplicate_permalink_and_output_collision_fail(self):
        p = self.post('new', permalink='/2000/01/01/old-one/')
        self.assertNotEqual(self.generate('new').returncode, 0)
        p.write_text(p.read_text().replace('/2000/01/01/old-one/', '/new/').replace('slug: "new"', 'slug: "old-one"'))
        self.assertNotEqual(self.generate('new').returncode, 0)
        self.assertEqual(self.snapshot(), self.before)

    def test_build_wrapper_does_not_render(self):
        (self.bin / 'pandoc').write_text('#!/bin/sh\nexit 99\n')
        self.assertEqual(self.run_script('maybe-export-post-pdfs.py').returncode, 0)
        self.assertEqual(self.snapshot(), self.before)

    @unittest.skipUnless(os.environ.get('BLOG_TEST_RENDER') == '1', 'Explicit cloud toolchain pilot only')
    def test_real_cloud_render(self):
        png(self.root / 'src/assets/pilot.png')
        self.post('pilot', 'Монгол кирилл: Өө Үү.\n\nMath: $x^2 + y^2 = z^2$.\n\n[Link](https://example.com/pilot)\n\n![Synthetic image](/blog/assets/pilot.png)')
        result = self.generate('pilot', real=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        pdf = self.root / 'src/assets/pdf/posts/2000/01/01/pilot.pdf'
        text = subprocess.check_output(['pdftotext', str(pdf), '-'], text=True)
        for phrase in ['Монгол', 'Өө', 'Үү', 'Math', 'Synthetic image']:
            self.assertIn(phrase, text)
        urls = subprocess.check_output(['pdfinfo', '-url', str(pdf)], text=True)
        self.assertIn('https://example.com/pilot', urls)
        images = subprocess.check_output(['pdfimages', '-list', str(pdf)], text=True)
        self.assertRegex(images, r'\b64\s+32\b')
        self.assertEqual(self.run_script('check-post-pdfs.py').returncode, 0)
        for path, data in self.before.items():
            if path.endswith('.pdf'): self.assertEqual((self.root / path).read_bytes(), data)
        # Optional durable private evidence outside this fixture/public checkout.
        if os.environ.get('BLOG_PILOT_OUTPUT'):
            out = Path(os.environ['BLOG_PILOT_OUTPUT']); out.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(pdf, out / 'synthetic-pilot.pdf')
            (out / 'synthetic-pilot.txt').write_text(text)
            (out / 'synthetic-pilot-inspection.json').write_text(json.dumps({'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(), 'pdf_bytes': pdf.stat().st_size, 'urls': urls, 'images': images, 'text_checks': ['Монгол', 'Өө', 'Үү', 'Math', 'Synthetic image'], 'historical_sentinel_pdfs_unchanged': True}, ensure_ascii=False, indent=2) + '\n')


class BuiltSiteTests(unittest.TestCase):
    run_script = PDFTests.run_script
    post = PDFTests.post
    snapshot = PDFTests.snapshot
    # Reuse only the fixture setup/helpers; the inherited PDF safety tests remain
    # in PDFTests and are not repeated here.
    def setUp(self):
        PDFTests.setUp(self)
        self.site = self.root / '_site'; self.site.mkdir()
        nav = '<nav class="site-nav"><a href="/blog/contents/">Гарчиг</a></nav>'
        for rel in ['index.html', 'archive/index.html', 'topics/index.html', 'tags/index.html', 'contents/index.html']:
            path = self.site / rel; path.parent.mkdir(parents=True, exist_ok=True); path.write_text(nav)
        for posturl, pdfurl in json.loads(self.mapping.read_text()).items():
            post = self.site / posturl.lstrip('/') / 'index.html'; post.parent.mkdir(parents=True, exist_ok=True)
            post.write_text(nav + f'<a class="pdf-download" href="{pdfurl}">PDF татах</a>')
            target = self.site / pdfurl.removeprefix('/blog/'); target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(self.root / 'src' / pdfurl.removeprefix('/blog/'), target)

    def test_built_pages_pass_and_missing_pdf_fails(self):
        self.assertEqual(self.run_script('check-built-site.py').returncode, 0)
        next((self.site / 'assets/pdf').rglob('*.pdf')).rename(self.root / 'temporarily-missing.pdf')
        result = self.run_script('check-built-site.py')
        self.assertNotEqual(result.returncode, 0); self.assertIn('Broken local PDF URL', result.stderr)

    def test_unconfigured_anchor_and_broken_navigation_fail(self):
        rogue = self.site / 'rogue.html'; rogue.write_text('<a class="pdf-download" href="https://example.com/rogue.pdf">PDF</a>')
        self.assertNotEqual(self.run_script('check-built-site.py').returncode, 0)
        rogue.write_text('')
        (self.site / 'contents/index.html').rename(self.root / 'temporarily-missing-page.html')
        result = self.run_script('check-built-site.py')
        self.assertNotEqual(result.returncode, 0); self.assertIn('Broken navigation link', result.stderr)


if __name__ == '__main__':
    unittest.main()
