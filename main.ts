// ai-excited-01 entry (Node 22, standard library only): the image beside this
// file is copied to /output/entry.png. The gate takes a whole PNG or JPEG of
// at most 1 MiB and 1024 by 1024 pixels; entry.png here is JPEG bytes under
// that name (told apart by its first bytes), 1024x1024, ~304 KB.
// The image was made for this competition: a humpback whale breaching out of
// a rooftop puddle at sunset, with a judge-addressed caption baked in.
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// package.json marks this directory an ES module so Node runs main.ts
// without the module-type warning.

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
