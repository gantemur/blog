# Migration Report

## Archive Inventory

- WordPress export archive: `source/wp_export.zip`
- Media archive: `source/wp_media.tar`
- Detected WXR/XML file: `t8m8r.wordpress.com-2026-07-06-13_57_43/t8m8r.wordpress.com.2026-07-06.000.xml`

## Detected Content

- Total WXR items: 1166
- Published posts: 207
- Published pages: 13
- Attachments in WXR: 914
- Media files in tar: 914
- Comments found: 273
- Approved comments written to private sanitized review: 268
- Categories: 40
- Tags: 615

## Import Result

- Markdown posts generated: 207
- Markdown pages generated: 13
- Media files copied: 914
- Media files skipped for unsafe paths or read errors: 0
- WordPress.com LaTeX snippets converted: 12422
- Caption shortcodes converted: 263
- Sourcecode shortcodes converted: 14

## Comments

Old WordPress comments are not rendered publicly. A sanitized review file was generated at `_import/comments-sanitized.jsonl` with post id/slug, display name, date, content, and optional author URL only. Email addresses, IP addresses, user-agent strings, and private metadata are not included.

## Private, Draft, or Unpublished Content

- Draft/private/unpublished posts/pages detected: 22
- Exported to ignored local archive: `_private/unpublished/`
- Exact titles and content are kept out of this public report.

## Shortcodes and Special Markup

- `n`: 73
- `x`: 26
- `gallery`: 11
- `m`: 6
- `L_1`: 2
- `L_2`: 2
- `A_nf`: 2
- `n-1`: 1
- `k-1`: 1
- `A_Tf`: 1

## Unresolved Media URLs

- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/ffgg.png (2)
- https://t8m8r.wordpress.com/wp-content/uploads/2010/04/berf1.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2010/04/berf32.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/psif.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/ffgg.png?w=640 (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/alim1.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/density.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/lild.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/lilg.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/lilgd.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/pnt3.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/psitheta11.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/gamlim.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2018/05/echeb.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2019/01/circle.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2019/01/semicircle.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2019/01/lemniscate-2.png (1)
- https://t8m8r.wordpress.com/wp-content/uploads/2020/12/png-image-2.png (1)

## Notes

- `source/`, `_import/`, `_tmp/`, `_site/`, and `node_modules/` are ignored by `.gitignore`.
- `_private/` is ignored by `.gitignore` and is used for local-only drafts and unpublished WordPress exports.
- Generated public Markdown, pages, and media live under `src/`.
- Site links are configured for the GitHub Pages project base path `/blog/`.
