# T8M8R Blog Migration

Static Eleventy blog migrated from `https://t8m8r.wordpress.com`, configured for GitHub Pages at:

https://gantemur.github.io/blog/

## Commands

```sh
npm install
npm run check
npm run build
npm run dev
npm run new -- "Post Title"
npm run new:draft -- "Post Title"
```

`source/` contains private WordPress export material and is ignored by git. Do not commit it. `_import/` contains private migration review files and reports, including sanitized comment review output; it is also ignored.

`npm run import:wordpress` is only for local migration or re-migration from private WordPress export files. Normal writing uses `npm run new -- "Post Title"`. Deployment builds from committed `src/` content only; GitHub Actions does not run the WordPress importer because `source/`, `_import/`, and `_private/` are intentionally ignored.

Run the WordPress importer only when you intentionally want to refresh the migrated Markdown from the private export files:

```sh
npm run import:wordpress
```

The importer reads the WXR XML directly from the zip archive and copies media from the tar archive into `src/assets/wp-media/`. Generated posts and pages live under `src/posts/` and `src/pages/` so the final static site can be built without publishing the raw WordPress export.

## LaTeX/PDF Export

Selected post sequences can be exported from committed source Markdown into a combined Pandoc-ready Markdown file:

```sh
npm run export:latex -- --manifest export/books/example.yml --out exports/example
```

Manifests live in `export/books/` and are intended to be tracked. A minimal manifest looks like:

```yml
title: "Эгэл бөөмсийн тэмдэглэл"
author: "Төмөр"
language: "mn"
division: "chapter"
posts:
  - /2023/05/03/chicago-pile/
  - /2023/05/04/jj/
```

You can also export links discovered from a topic/contents page, optionally limited to one section:

```sh
python3 scripts/export-latex.py --contents src/pages/808-physics.md --section "Атом, цөм, эгэл бөөмс" --out exports/physics-particles
```

The exporter writes `book.md` and `manifest-resolved.json`. If Pandoc is installed, it also writes `book.tex`; otherwise it prints the Pandoc command to run later. `book.tex` references image files; it does not embed them, so keep the generated `assets/` directory beside the book source or make it reachable through Pandoc’s `--resource-path`.

To ask the exporter to create a PDF as well:

```sh
npm run export:latex -- --manifest export/books/example.yml --out exports/example --pdf --pdf-engine xelatex --mainfont "Times New Roman"
```

For Mongolian exports, figure and table captions default to `Зураг` and `Хүснэгт`. Override them when needed with `--figure-name "Зураг"` and `--table-name "Хүснэгт"` or the manifest fields `figureName` and `tableName`.

For a PDF with Mongolian Cyrillic, use XeLaTeX or LuaLaTeX. From inside the export directory:

```sh
cd exports/example
pandoc book.md --pdf-engine=xelatex -V mainfont="Times New Roman" -o book.pdf
```

Or from the repository root:

```sh
pandoc exports/example/book.md \
  --resource-path=exports/example \
  --pdf-engine=xelatex \
  -V mainfont="Times New Roman" \
  -o exports/example/book.pdf
```

Generated `exports/` output is ignored by git by default. Commit selected export sources only if a particular book project should become part of the repository.

## Old WordPress Comments

Old WordPress comments were exported from the WXR file, but they are not rendered on the public site. The importer writes a sanitized local review file to `_import/comments-sanitized.jsonl` with only public-looking fields: post id/slug, display name, date, content, and optional author URL.

Commenter email addresses, IP addresses, user-agent strings, and private WordPress metadata are intentionally stripped. Later, approved old comments can be reviewed manually and, if desired, converted into static archived comments.

## New Comments With Giscus

Giscus support is prepared in `src/_includes/comments.njk` and configured in `src/_data/site.json`, but it is disabled by default. To enable it later:

1. Create and push the GitHub repo `gantemur/blog`.
2. Enable GitHub Discussions for the repo.
3. Install or enable the giscus GitHub app for the repo.
4. Go to `https://giscus.app`.
5. Select repo `gantemur/blog`.
6. Choose mapping `pathname`.
7. Choose category `Blog comments`.
8. Copy the generated repo/category IDs into `src/_data/site.json`.
9. Set `comments.enabled` to `true`.
10. Rebuild and deploy.

Per-post front matter can set `comments: true` or `comments: false`. Comments render only when global comments are enabled and the post has not opted out.

## Unpublished WordPress Content

Draft/private/unpublished WordPress posts and pages are preserved locally in `_private/unpublished/`. That folder is ignored by git and must stay out of the public repository.

To publish one later, manually review it, remove private or unfinished material, then move or copy it into `src/posts/` or `src/pages/` with suitable front matter.

## New Post Workflow

Create a normal new post:

```sh
npm run new -- "Post Title"
```

This creates a Markdown file under `src/posts/` with today’s date, a slug from the title, `comments: true`, and `draft: false`.

There are two kinds of drafts:

- Public-source drafts: create or edit a file in `src/posts/` and set `draft: true`. Production builds exclude it, but it is still visible in GitHub source if committed.
- Private local drafts: use `_private/drafts/`, which is ignored by git and safest for genuinely private or unfinished writing.

Create a private local draft:

```sh
npm run new:draft -- "Post Title"
```

Production builds exclude posts with `draft: true`. `npm run check` reports the number of draft posts currently in public source.
