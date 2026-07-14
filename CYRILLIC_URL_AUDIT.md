# Cyrillic URL Audit

Audit scope: source filenames under `src/posts`, `src/pages`, `src/aliases`; front matter `slug` and `permalink`; percent-encoded values that decode to Cyrillic; and category/tag page generators. Titles and visible Mongolian text are intentionally out of scope.

## Summary

- Cyrillic/non-ASCII source post filenames: 0
- Cyrillic/non-ASCII source page filenames: 0
- Cyrillic/non-ASCII alias filenames: 0
- Literal non-ASCII canonical post/page slugs: 0
- Percent-encoded canonical post/page slugs that decode to Cyrillic/non-ASCII: 0
- Literal non-ASCII canonical post/page permalinks: 0
- Percent-encoded canonical post/page permalinks that decode to Cyrillic/non-ASCII: 0
- Percent-encoded alias permalinks that preserve old Cyrillic URLs: 3
- Percent-encoded WordPress source URLs that decode to Cyrillic/non-ASCII: 3

## 1. Cyrillic/non-ASCII source post filenames

None found.

## 2. Cyrillic/non-ASCII source page filenames

None found.

## 3. Cyrillic/non-ASCII alias filenames

None found.

## 4. Literal non-ASCII canonical post/page slugs

None found.

## 5. Percent-encoded canonical post/page slugs that decode to Cyrillic/non-ASCII

None found.

## 6. Literal non-ASCII canonical post/page permalinks

None found.

## 7. Percent-encoded canonical post/page permalinks that decode to Cyrillic/non-ASCII

None found.

## 8. Alias permalinks preserving old Cyrillic URLs

- `src/aliases/2009__08__20__torsor-cyrillic-old.njk`: `/2009/08/20/%d1%82%d0%be%d1%80%d1%81%d0%be%d1%80-%d0%b3%d1%8d%d0%b6-%d1%8e%d1%83-%d0%b2%d1%8d/` -> `/2009/08/20/торсор-гэж-юу-вэ/`
- `src/aliases/2010__02__23__hanging-a-picture-cyrillic-old.njk`: `/2010/02/23/%d0%b7%d1%83%d1%80%d0%b0%d0%b3-%d3%a9%d0%bb%d0%b3%d3%a9%d1%85/` -> `/2010/02/23/зураг-өлгөх/`
- `src/aliases/2024__03__17__texas-cyrillic-old.njk`: `/2024/03/17/%d1%82%d0%b5%d1%85%d0%b0%d1%81-%d0%bd%d1%8d%d1%80%d0%bd%d0%b8%d0%b9-%d1%83%d1%87%d0%b8%d1%80/` -> `/2024/03/17/техас-нэрний-учир/`

## 9. Category/tag pages with Cyrillic paths

Category and tag archive URLs are generated from category/tag names. Because many categories/tags are Mongolian Cyrillic, their generated paths are expected to be percent-encoded Cyrillic paths. This is separate from post/page canonical slugs and is intentionally left unchanged.

- `src/category-pages.njk`: generator present; slug/filter usage detected: `True`
- `src/tag-pages.njk`: generator present; slug/filter usage detected: `False`

## 10. Harmless / should stay

- Mongolian Cyrillic titles, headings, tags, categories, and visible text should stay.
- Alias permalinks for old Cyrillic URLs should stay, because they preserve old WordPress/GitHub Pages routes.
- Historical `wordpress_url` fields should stay, because they record source URLs rather than canonical generated routes.
- Category/tag archive paths may remain Cyrillic/percent-encoded unless there is a separate taxonomy URL policy change.

## 11. Probable ASCII-rename candidates

No remaining canonical post/page filenames, alias filenames, slugs, or permalinks require ASCII renaming.


## 12. Old URLs needing aliases if renamed

- `/2009/08/20/%d1%82%d0%be%d1%80%d1%81%d0%be%d1%80-%d0%b3%d1%8d%d0%b6-%d1%8e%d1%83-%d0%b2%d1%8d/` from `src/aliases/2009__08__20__torsor-cyrillic-old.njk` redirects to `/2009/08/20/torsor/`.
- `/2010/02/23/%d0%b7%d1%83%d1%80%d0%b0%d0%b3-%d3%a9%d0%bb%d0%b3%d3%a9%d1%85/` from `src/aliases/2010__02__23__hanging-a-picture-cyrillic-old.njk` redirects to `/2010/02/23/hanging-a-picture/`.
- `/2024/03/17/%d1%82%d0%b5%d1%85%d0%b0%d1%81-%d0%bd%d1%8d%d1%80%d0%bd%d0%b8%d0%b9-%d1%83%d1%87%d0%b8%d1%80/` from `src/aliases/2024__03__17__texas-cyrillic-old.njk` redirects to `/2024/03/17/texas/`.

## 13. WordPress source URLs with encoded Cyrillic paths

These are historical source references, not canonical generated URLs. They matter for importer/export resolver coverage but are not route blockers.

- `src/posts/2009-08-20-113-torsor.md`: `https://t8m8r.wordpress.com/2009/08/20/%d1%82%d0%be%d1%80%d1%81%d0%be%d1%80-%d0%b3%d1%8d%d0%b6-%d1%8e%d1%83-%d0%b2%d1%8d/` -> `https://t8m8r.wordpress.com/2009/08/20/торсор-гэж-юу-вэ/`
- `src/posts/2010-02-23-127-hanging-a-picture.md`: `https://t8m8r.wordpress.com/2010/02/23/%d0%b7%d1%83%d1%80%d0%b0%d0%b3-%d3%a9%d0%bb%d0%b3%d3%a9%d1%85/` -> `https://t8m8r.wordpress.com/2010/02/23/зураг-өлгөх/`
- `src/posts/2024-03-17-5738-texas.md`: `https://t8m8r.wordpress.com/2024/03/17/%d1%82%d0%b5%d1%85%d0%b0%d1%81-%d0%bd%d1%8d%d1%80%d0%bd%d0%b8%d0%b9-%d1%83%d1%87%d0%b8%d1%80/` -> `https://t8m8r.wordpress.com/2024/03/17/техас-нэрний-учир/`
