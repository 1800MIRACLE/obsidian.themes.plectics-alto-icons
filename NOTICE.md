# Notices

Plectics Alto, an Obsidian theme. Copyright © 2026 1800MIRACLE.
Licensed under the GNU General Public License, version 3 (see `LICENSE`).
Repository: https://github.com/1800MIRACLE/obsidian.themes.plectics-alto

This notice covers both themes built from that repository, Plectics Alto and
Plectics Alto Icons (https://github.com/1800MIRACLE/obsidian.themes.plectics-alto-icons).
File paths below refer to the Plectics Alto repository. The Icons repository
carries the licence texts in `licences/`.

The built `theme.css` embeds the assets below. Each keeps its own licence; the
GPL-3.0 covers the theme's own code and does not change those terms.

## Fonts embedded in `theme.css` (as woff2 subsets, base64)

**Alto Garamond Condensed** (Regular, Italic; the repository also has Medium,
Bold and their italics as TTF). A derivative of EB Garamond, Copyright 2017 The EB Garamond
Project Authors (https://github.com/octaviopardo/EBGaramond12). It is condensed
horizontally to 80 % with weight compensation by `fonts/build/`, and renamed.
Licensed under the SIL Open Font License 1.1: `fonts/OFL-EBGaramond.txt`.
EB Garamond declares no Reserved Font Name.

**PLX Caps**: Nimbus Sans Regular and Bold, Copyright (URW)++ Design &
Development, from urw-base35 (https://github.com/ArtifexSoftware/urw-base35-fonts).
Licensed under the GNU Affero General Public License, version 3: `fonts/nimbus/COPYING`
and `fonts/nimbus/LICENSE`. The font exception in that LICENSE covers only
PostScript and PDF embedding, so the full AGPL-3.0 applies to the copy embedded
here. The embedded copy is a subset, with no other modification. Its
corresponding source is `fonts/nimbus/NimbusSans-*.otf` and
`fonts/build/make_web_subsets.py`. GPL-3.0 and AGPL-3.0 allow the combination
(section 13 of each).

**Archivo** (interface face, weights 100–900, width 100), Copyright 2020 The
Archivo Project Authors (https://github.com/Omnibus-Type/Archivo). Licensed under
the SIL Open Font License 1.1: `fonts/archivo/OFL-Archivo.txt`. Subset and
pinned to width 100 by `fonts/build/make_web_subsets.py`.

## Icons

**Farm-Fresh Web Icons** v3.92 by FatCow Web Hosting
(https://www.fatcow.com/free-icons), licensed under Creative Commons Attribution
3.0 United States (https://creativecommons.org/licenses/by/3.0/us/). They are used
in **Plectics Alto Icons** only (`icons/farm-fresh/`, embedded by
`gen_farmfresh.py`). Thirteen icons are composed from Farm-Fresh parts
(`ff-compose/`; the theme uses twelve of them): these are changed versions of
the originals, under the same licence.

**Lucide** icons (the line icons of the file list, embedded as SVG masks in
`src/a-base/20-file-tree.css`), Copyright (c) Lucide Contributors
(https://lucide.dev). ISC License. Some Lucide icons come from Feather, Copyright
(c) 2013-2023 Cole Bemis, MIT License.

> ISC License: Permission to use, copy, modify, and/or distribute this software
> for any purpose with or without fee is hereby granted, provided that the above
> copyright notice and this permission notice appear in all copies. THE SOFTWARE
> IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
> SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS. IN NO
> EVENT SHALL THE AUTHOR BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
> CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE,
> DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS
> ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS
> SOFTWARE.

## Fonts named but not shipped

The theme names some fonts in its font stacks. A named font is used only if it
is installed on your computer; none of these is included:
- ChicagoFLF (public domain, by Robin Casady after Susan Kare's Chicago);
- Apple Garamond and Berkeley Mono, both commercial;
- EB Garamond, IBM Plex, CMU Serif, Inter, Instrument Sans, Golos Text and
  JetBrains Mono, all SIL OFL 1.1;
- Constantia, Segoe UI, Georgia, Consolas and Arial, all system fonts.

If a named font is not installed, the next font in the stack is used.
