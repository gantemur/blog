#!/usr/bin/env python3
"""Validate rendered public posts, navigation, and optional PDF download URLs."""
import importlib.util
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / '_site'
spec = importlib.util.spec_from_file_location('pdfcheck', ROOT / 'scripts/check-post-pdfs.py')
PDF = importlib.util.module_from_spec(spec)
spec.loader.exec_module(PDF)


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.pdfs = []
        self.navigation = []
        self.in_nav = False

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == 'nav' and 'site-nav' in a.get('class', '').split():
            self.in_nav = True
        if tag == 'a':
            if 'pdf-download' in a.get('class', '').split():
                self.pdfs.append(a.get('href', ''))
            if self.in_nav:
                self.navigation.append(a.get('href', ''))

    def handle_endtag(self, tag):
        if tag == 'nav':
            self.in_nav = False


def output_path(url):
    parts = urlsplit(url)
    if parts.scheme or parts.netloc:
        return None
    path = unquote(parts.path)
    if path.startswith('/blog/'):
        path = path.removeprefix('/blog/')
    else:
        path = path.lstrip('/')
    target = SITE / path
    if path.endswith('/') or not path:
        target /= 'index.html'
    if not target.resolve().is_relative_to(SITE.resolve()):
        raise ValueError('URL escapes build output')
    return target


def main():
    errors = []
    mapping = json.loads((ROOT / 'src/_data/post_pdfs.json').read_text())
    expected = {}
    posts = 0
    for source in sorted((ROOT / 'src/posts').glob('*.md')):
        front = PDF.read_front_matter(source)
        if front.get('draft') is True or front.get('status') in ('draft', 'private'):
            continue
        posts += 1
        url = str(front.get('permalink', ''))
        if not url.startswith('/'):
            errors.append(f'{source.name}: missing absolute permalink')
            continue
        path = output_path(url)
        if path in expected:
            errors.append(f'Duplicate rendered permalink: {url}')
        config = PDF.pdf_config(front)
        pdfurl = ''
        if config.get('enabled'):
            pdfurl = str(config.get('url') or mapping.get(url, ''))
            if pdfurl.startswith('/') and not pdfurl.startswith('/blog/'):
                pdfurl = '/blog' + pdfurl
            if not pdfurl:
                errors.append(f'{source.name}: enabled PDF has no URL')
        expected[path] = [pdfurl] if pdfurl else []
        if not path.is_file():
            errors.append(f'Missing rendered post: {url}')
    found_links = 0
    for path in SITE.rglob('*.html'):
        links = Links(); links.feed(path.read_text(encoding='utf-8'))
        if links.pdfs != expected.get(path, []):
            errors.append(f'Unexpected PDF download anchors: {path.relative_to(SITE)}')
        found_links += len(links.pdfs)
        for url in links.pdfs:
            target = output_path(url)
            if target is not None and not target.is_file():
                errors.append(f'Broken local PDF URL: {url}')
    for url in ['/', '/archive/', '/topics/', '/tags/']:
        path = output_path(url)
        if not path.is_file():
            errors.append(f'Missing navigation page: {url}')
            continue
        links = Links(); links.feed(path.read_text(encoding='utf-8'))
        if not links.navigation:
            errors.append(f'Missing site navigation: {url}')
        for target_url in links.navigation:
            target = output_path(target_url)
            if target is not None and not target.is_file():
                errors.append(f'Broken navigation link: {target_url}')
    for private in ['source', '_private', '_import', 'sources']:
        if (SITE / private).exists():
            errors.append(f'Private directory in build output: {private}')
    if errors:
        raise SystemExit('\n'.join(errors))
    print(f'Built site passed: {posts} public posts; {found_links} PDF download links; navigation and local PDF URLs resolve.')


if __name__ == '__main__':
    main()
