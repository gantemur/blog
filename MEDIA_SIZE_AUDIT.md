# Media Size Audit

Audit date: 2026-07-14

Scope: repository and media size only. No images were optimized, resized, deleted, rewritten, or moved during this pass.

## Summary

- Overall working tree: `2.2G`.
- Committed WordPress media under `src/assets/wp-media`: `347M`.
- Git loose object store: `323.96 MiB`.
- The largest tracked files are media files, mostly imported WordPress images and GIFs.
- The working tree is larger than tracked source media because generated/ignored build output is present locally: `_site` is `647M`, `exports` is `551M`, and `.git` is `324M`.

## 1. Overall Working Tree Size

Command:

```sh
du -sh .
```

Output:

```text
2.2G	.
```

Command:

```sh
du -sh src/assets src/assets/wp-media 2>/dev/null || true
```

Output:

```text
347M	src/assets
347M	src/assets/wp-media
```

Additional local context:

```text
324M	.git
647M	_site
551M	exports
350M	src
 22M	node_modules
```

## 2. Git Object Size

Command:

```sh
git count-objects -vH
```

Output:

```text
count: 1657
size: 323.96 MiB
in-pack: 0
packs: 0
size-pack: 0 bytes
prune-packable: 0
garbage: 0
size-garbage: 0 bytes
```

## 3. Largest Tracked Files

Command:

```sh
git ls-files -z | xargs -0 du -h | sort -h | tail -50
```

Output:

```text
1.3M	src/assets/wp-media/2020/04/ptolplan.png
1.3M	src/assets/wp-media/2020/05/starwheel_47n_mn.png
1.4M	src/assets/wp-media/2017/03/equinox3.jpg
1.4M	src/assets/wp-media/2020/03/animated_hippopede_of_eudoxus.gif
1.4M	src/assets/wp-media/2020/04/26297.jpg
1.4M	src/assets/wp-media/2020/05/azalteqot.png
1.4M	src/assets/wp-media/2020/05/d0g41trw0aimo0e.jpeg
1.4M	src/assets/wp-media/2020/05/melbourne_sundial_at_flagstaff_gardens.jpg
1.4M	src/assets/wp-media/2020/05/rete.jpg
1.5M	src/assets/wp-media/2018/09/gd3.png
1.5M	src/assets/wp-media/2020/05/astrolabe_rete.jpg
1.5M	src/assets/wp-media/2020/05/dgjqtnfv4aanmmx.jpeg
1.6M	src/assets/wp-media/2020/12/1cqxc6gsvnycncgptpd8era.png
1.7M	src/assets/wp-media/2020/05/astrolabe_tympan.jpg
1.8M	src/assets/wp-media/2017/10/giphy.gif
2.0M	src/assets/wp-media/2017/12/crow.gif
2.0M	src/assets/wp-media/2017/12/ezgif-com-optimize.gif
2.0M	src/assets/wp-media/2020/05/scales.jpg
2.1M	src/assets/wp-media/2020/03/december_10th_lunar_eclipse.jpg
2.1M	src/assets/wp-media/2020/04/armillary_sphere_in_esrin.jpg
2.2M	src/assets/wp-media/2018/01/newtime.jpg
2.2M	src/assets/wp-media/2018/01/newtime1.jpg
2.2M	src/assets/wp-media/2018/01/newtime2.jpg
2.3M	src/assets/wp-media/2020/05/azimuthalmap.png
2.4M	src/assets/wp-media/2020/05/astrolabe_comp.jpg
2.4M	src/assets/wp-media/2020/05/world_time_zones_map.png
2.5M	src/assets/wp-media/2018/01/newtime3.jpg
2.5M	src/assets/wp-media/2019/03/inscription_on_broom_bridge_dublin_regarding_the_discovery_of_quaternions_multiplication_by_sir_william_rowan_hamilton.jpg
2.6M	src/assets/wp-media/2020/05/back.jpg
2.8M	src/assets/wp-media/2017/11/rotref3.jpg
2.9M	src/assets/wp-media/2017/11/rot3.jpg
3.0M	src/assets/wp-media/2020/05/astrolabe_proj.jpg
3.5M	src/assets/wp-media/2023/05/screen-shot-2023-05-04-at-17.59.43.png
3.7M	src/assets/wp-media/2019/10/pe_77a.jpg
3.7M	src/assets/wp-media/2020/05/sundial_-_melbourne_planetarium.jpg
3.8M	src/assets/wp-media/2025/09/screenshot-2025-09-07-at-13.18.18.png
3.8M	src/assets/wp-media/2025/09/screenshot-2025-09-07-at-13.22.25.png
3.9M	src/assets/wp-media/2017/11/qt.gif
3.9M	src/assets/wp-media/2019/06/ktfc1.jpg
4.0M	src/assets/wp-media/2020/05/tympan.jpg
4.2M	src/assets/wp-media/2018/08/nn-3.png
4.2M	src/assets/wp-media/2020/05/decoding_an_ancient_computer.jpg
4.4M	src/assets/wp-media/2020/05/decoding_an_ancient_computer-1.jpg
4.5M	src/assets/wp-media/2020/05/tympan-1.jpg
4.7M	src/assets/wp-media/2017/11/so3.jpg
4.9M	src/assets/wp-media/2020/03/1pzesamfopxgyjboqvtpmjq.gif
5.0M	src/assets/wp-media/2017/11/rp3.jpg
5.7M	src/assets/wp-media/2015/09/star_trails_over_the_eso_3-6-metre_telescope.jpg
8.0M	src/assets/wp-media/2020/03/all_in_a_spin_star_trail.jpg
 19M	src/assets/wp-media/2017/12/giphy-2.gif
```

## 4. Largest Media Files

Command:

```sh
find src/assets -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.webp" -o -iname "*.pdf" \) -print0 \
  | xargs -0 du -h | sort -h | tail -50
```

Output matched the largest tracked files above. In this repository snapshot, the largest tracked files are all media files under `src/assets/wp-media`.

## 5. Media Counts And Total Sizes By Extension

```text
.jpg	436	202.88 MiB
.png	423	98.66 MiB
.gif	18	37.57 MiB
.jpeg	33	4.81 MiB
.pdf	4	0.91 MiB
TOTAL	914	344.83 MiB
```

Additional media count:

```text
914 media files under src/assets
35 media files larger than 2 MiB
```

## 6. Recommendations

- The tracked repository size is mostly imported media. Source Markdown and templates are small compared with `src/assets/wp-media`.
- Lossless optimization could help, especially for PNG files and some GIFs, but likely will not radically change the repo if the largest files are already compressed photos or animations.
- Visually lossless resizing could help more for very large screenshots, photos, and GIFs that are displayed at blog-column width. The 19M GIF and several 4-8M images are the first candidates for a later manual review.
- Since these media files have already been committed and pushed, optimizing files in a normal future commit would reduce checkout/build size going forward but would not truly shrink existing Git history.
- To truly shrink already-pushed repository history, a deliberate history rewrite would be required. That should be treated as a separate, coordinated operation because it affects every clone and remote reference.
- If full-resolution originals should be preserved, keep them in ignored/private storage in the future and commit web-sized derivatives only.
- Generated local directories such as `_site` and `exports` are large but ignored build artifacts. They affect local disk usage, not committed repository source size.

## 7. Future Per-Post PDF Design Note

Do not generate PDFs for all posts automatically and do not run TeX/Pandoc for all posts in GitHub Actions.

A safer future design:

- Add front matter to selected posts only:

```yml
pdf: true
```

- Generate selected post PDFs locally into a committed asset path such as:

```text
src/assets/pdf/posts/YYYY/MM/DD/slug.pdf
```

- Generate a small data map:

```text
src/_data/post_pdfs.json
```

- Later, modify the post layout to show `PDF татах` only when the PDF exists or when front matter enables it.

This keeps expensive PDF generation local and intentional while allowing selected finished PDFs to be committed and served as static assets.
