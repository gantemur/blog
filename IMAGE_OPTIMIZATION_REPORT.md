# Image Optimization Report

- Date: 2026-07-14T15:55:56+08:00
- Mode: `apply`
- Command: `python3 scripts/optimize-media.py --apply`
- Target: `src/assets/wp-media`
- Backup directory: `_private/media-originals`
- Minimum size: `1.5M`
- Max long edge: `2200`
- JPEG quality: `88`
- Current target size: `266.5M`

## Summary

- Candidates considered: 39
- Optimized files: 30
- Skipped files: 9
- Original total size of optimized files: 98.9M
- New total size of optimized files: 20.6M
- Estimated/actual savings: 78.3M

Normal commits reduce current and future checkout size, but they do not shrink already-pushed Git history.

## Optimized Files

- `src/assets/wp-media/2015/09/star_trails_over_the_eso_3-6-metre_telescope.jpg`: 5.7M -> 1.3M (3456x2304 -> 2200x1467, saved 4.4M)
- `src/assets/wp-media/2017/11/rot3.jpg`: 2.9M -> 155.8K (6666x6844 -> 2143x2200, saved 2.7M)
- `src/assets/wp-media/2017/11/rotref3.jpg`: 2.8M -> 136.2K (6399x6844 -> 2057x2200, saved 2.7M)
- `src/assets/wp-media/2017/11/rp3.jpg`: 5.0M -> 330.1K (6843x6844 -> 2200x2200, saved 4.7M)
- `src/assets/wp-media/2017/11/so3.jpg`: 4.7M -> 263.3K (6843x6844 -> 2200x2200, saved 4.5M)
- `src/assets/wp-media/2018/01/newtime.jpg`: 2.2M -> 249.5K (3149x1520 -> 2200x1062, saved 2.0M)
- `src/assets/wp-media/2018/01/newtime1.jpg`: 2.2M -> 244.9K (3149x1520 -> 2200x1062, saved 1.9M)
- `src/assets/wp-media/2018/01/newtime2.jpg`: 2.2M -> 239.5K (3149x1520 -> 2200x1062, saved 1.9M)
- `src/assets/wp-media/2018/01/newtime3.jpg`: 2.5M -> 272.6K (3149x1520 -> 2200x1062, saved 2.2M)
- `src/assets/wp-media/2019/03/inscription_on_broom_bridge_dublin_regarding_the_discovery_of_quaternions_multiplication_by_sir_william_rowan_hamilton.jpg`: 2.5M -> 818.7K (3803x2487 -> 2200x1439, saved 1.7M)
- `src/assets/wp-media/2019/06/ktfc1.jpg`: 3.9M -> 542.3K (6384x2099 -> 2200x723, saved 3.4M)
- `src/assets/wp-media/2019/10/pe_77a.jpg`: 3.7M -> 1.6M (2625x3089 -> 1870x2200, saved 2.1M)
- `src/assets/wp-media/2020/03/all_in_a_spin_star_trail.jpg`: 8.0M -> 951.7K (5616x3744 -> 2200x1467, saved 7.1M)
- `src/assets/wp-media/2020/03/december_10th_lunar_eclipse.jpg`: 2.1M -> 495.9K (1920x1280 -> 1920x1280, saved 1.6M)
- `src/assets/wp-media/2020/04/armillary_sphere_in_esrin.jpg`: 2.1M -> 784.7K (2881x1621 -> 2200x1238, saved 1.4M)
- `src/assets/wp-media/2020/05/astrolabe_comp.jpg`: 2.4M -> 331.2K (3602x3298 -> 2200x2014, saved 2.1M)
- `src/assets/wp-media/2020/05/astrolabe_proj.jpg`: 3.0M -> 313.1K (3365x3255 -> 2200x2128, saved 2.7M)
- `src/assets/wp-media/2020/05/astrolabe_rete.jpg`: 1.5M -> 156.3K (3365x1596 -> 2200x1043, saved 1.4M)
- `src/assets/wp-media/2020/05/astrolabe_tympan.jpg`: 1.7M -> 157.5K (3365x1588 -> 2200x1038, saved 1.6M)
- `src/assets/wp-media/2020/05/azimuthalmap.png`: 2.3M -> 2.1M (3919x3901 -> 2200x2190, saved 264.5K)
- `src/assets/wp-media/2020/05/back.jpg`: 2.6M -> 537.8K (3467x3403 -> 2200x2159, saved 2.1M)
- `src/assets/wp-media/2020/05/decoding_an_ancient_computer-1.jpg`: 4.4M -> 297.8K (3860x3147 -> 2200x1794, saved 4.1M)
- `src/assets/wp-media/2020/05/decoding_an_ancient_computer.jpg`: 4.2M -> 296.7K (3860x3147 -> 2200x1794, saved 3.9M)
- `src/assets/wp-media/2020/05/scales.jpg`: 2.0M -> 322.2K (2989x1912 -> 2200x1407, saved 1.7M)
- `src/assets/wp-media/2020/05/sundial_-_melbourne_planetarium.jpg`: 3.7M -> 466.3K (4658x1690 -> 2200x798, saved 3.3M)
- `src/assets/wp-media/2020/05/tympan-1.jpg`: 4.5M -> 459.5K (3956x3809 -> 2200x2118, saved 4.0M)
- `src/assets/wp-media/2020/05/tympan.jpg`: 4.0M -> 443.8K (3956x3809 -> 2200x2118, saved 3.6M)
- `src/assets/wp-media/2020/05/world_time_zones_map.png`: 2.4M -> 1.7M (4000x2157 -> 2200x1186, saved 712.2K)
- `src/assets/wp-media/2025/09/screenshot-2025-09-07-at-13.18.18.png`: 3.8M -> 2.4M (2992x1680 -> 2200x1235, saved 1.3M)
- `src/assets/wp-media/2025/09/screenshot-2025-09-07-at-13.22.25.png`: 3.8M -> 2.5M (2992x1934 -> 2200x1422, saved 1.3M)

## Skipped Large GIFs

- `src/assets/wp-media/2017/10/giphy.gif`: 1.8M
- `src/assets/wp-media/2017/11/qt.gif`: 3.9M
- `src/assets/wp-media/2017/12/crow.gif`: 2.0M
- `src/assets/wp-media/2017/12/ezgif-com-optimize.gif`: 2.0M
- `src/assets/wp-media/2017/12/giphy-2.gif`: 19.4M
- `src/assets/wp-media/2020/03/1pzesamfopxgyjboqvtpmjq.gif`: 4.9M

## Skipped Large PNGs

- `src/assets/wp-media/2018/08/nn-3.png`: 4.2M (large PNG has no resize opportunity; not converting PNG to JPEG)
- `src/assets/wp-media/2020/12/1cqxc6gsvnycncgptpd8era.png`: 1.6M (large PNG has no resize opportunity; not converting PNG to JPEG)

## Skipped Large WEBPs

- None

## Other Skipped Large Files

- `src/assets/wp-media/2023/05/screen-shot-2023-05-04-at-17.59.43.png`: 3.5M (optimized file was not smaller)
