# T8M8R Blog Migration

Static Eleventy blog migrated from `https://t8m8r.wordpress.com`, configured for GitHub Pages at:

https://gantemur.github.io/blog/

## Commands

```sh
npm install
npm run import:wordpress
npm run check
npm run build
npm run dev
npm run new -- "Post Title"
npm run new:draft -- "Post Title"
```

`source/` contains private WordPress export material and is ignored by git. Do not commit it. `_import/` contains private migration review files and reports, including sanitized comment review output; it is also ignored.

`npm run import:wordpress` is only for local migration or re-migration from private WordPress export files. Normal writing uses `npm run new -- "Post Title"`. Deployment builds from committed `src/` content only; GitHub Actions does not run the WordPress importer because `source/`, `_import/`, and `_private/` are intentionally ignored.

The importer reads the WXR XML directly from the zip archive and copies media from the tar archive into `src/assets/wp-media/`. Generated posts and pages live under `src/posts/` and `src/pages/` so the final static site can be built without publishing the raw WordPress export.

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
