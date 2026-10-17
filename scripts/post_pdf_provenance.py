"""Byte-based provenance for generated PDFs; no checkout timestamp assumptions."""
import hashlib
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def asset_hashes(root, post):
    """Track local Markdown/HTML image inputs used by the existing exporter.

    Relative images resolve from repository root, as in Pandoc's resource path.
    External images are rejected for generated PDFs: vendor reviewed assets first.
    """
    text = post.read_text(encoding='utf-8')
    urls = re.findall(r'!\[[^\]]*\]\(<?([^\s)>]+)>?(?:\s+[^)]*)?\)', text)
    urls += re.findall(r'<img\b[^>]*\bsrc=[\"\']([^\"\']+)', text, re.I)
    # Pandoc reference-style image definitions may also supply image resources.
    references = {k.lower(): v for k, v in re.findall(r'^\s*\[([^\]]+)\]:\s*<?([^\s>]+)>?', text, re.M)}
    for alt, label in re.findall(r'!\[([^\]]*)\]\[([^\]]*)\]', text):
        key = (label or alt).lower()
        if key not in references:
            raise ValueError(f'Unresolved image reference: {key}')
        urls.append(references[key])
    result = {}
    for url in urls:
        parts = urlsplit(url)
        if parts.scheme or parts.netloc:
            raise ValueError('Generated PDFs require reviewed local image assets')
        path = unquote(parts.path)
        if path.startswith('/blog/assets/'):
            path = 'src/assets/' + path.removeprefix('/blog/assets/')
        elif path.startswith('/assets/'):
            path = 'src/assets/' + path.removeprefix('/assets/')
        target = (root / path).resolve()
        if not target.is_relative_to(root.resolve()) or not target.is_file():
            raise ValueError(f'Missing or out-of-repository image: {path}')
        result[target.relative_to(root).as_posix()] = digest(target)
    return dict(sorted(result.items()))


def source_record(root, post, pdf, renderer):
    return {'source': post.relative_to(root).as_posix(), 'source_sha256': digest(post),
            'pdf_sha256': digest(pdf), 'assets': asset_hashes(root, post),
            'renderer': renderer}


def validate_record(root, post, pdf, record):
    if not isinstance(record, dict):
        return 'missing PDF provenance; explicitly regenerate this post'
    if record.get('source') != post.relative_to(root).as_posix() or record.get('source_sha256') != digest(post):
        return 'PDF source changed; regenerate or review a documented provenance exception'
    if record.get('pdf_sha256') != digest(pdf):
        return 'PDF bytes differ from provenance'
    try:
        if record.get('assets') != asset_hashes(root, post):
            return 'PDF image assets changed; regenerate the PDF'
    except ValueError as error:
        return str(error)
    if not record.get('renderer') and not record.get('exception'):
        return 'provenance needs renderer metadata or a documented exception'
    return None
