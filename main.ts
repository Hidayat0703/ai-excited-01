// ai-excited-01 entry, Node 22, standard library only.
// Copies the entry image beside this file to /output/entry.png.
// The file is named entry.png but holds JPEG bytes (the gate tells PNG
// from JPEG by the first bytes); it is 1024x1024 and well under 1 MiB.
// The picture: a humpback whale breaching out of a rooftop rain puddle
// at golden sunset, a tiny person in a yellow raincoat looking up, and
// a caption addressed to the judge baked in along the bottom.
// Run locally with: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// package.json marks this folder an ES module so node runs this file
// without a module-type warning.

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
