# Plectics Alto Icons community submission

Prepared on 2026-11-17 for the `a1126` branch. This is preparation material; no community submission or release has been published by this work.

## Current submission route

Submit through [Obsidian Community](https://community.obsidian.md), after merging the implementation into this repository's default branch and publishing its release. The [official theme submission guide](https://docs.obsidian.md/Themes/App%20themes/Submit%20your%20theme) now uses the directory rather than an `obsidian-releases` pull request. The owner signs in, connects GitHub, adds the repository, and addresses the directory's review feedback.

The old theme/plugin PR templates were [removed on 2026-05-15](https://github.com/obsidianmd/obsidian-releases/commit/d4f069442f61bb055e899cbed7c0c03b5e5c8744). The JSON and PR text below preserve the requested historical format for reference; they are not instructions to open a new upstream PR.

## Directory fields

- Repository: `https://github.com/1800MIRACLE/obsidian.themes.plectics-alto-icons`
- Name: **Plectics Alto Icons**
- Author: **1800MIRACLE**
- Supported modes: **Light and Dark**
- Screenshot: `screenshots/preview.png` (captured in an isolated Obsidian test vault).
- Description: **A light and dark theme with colour icons for research notes, with serif typography, compact desktop-style controls, and dedicated styling for mathematical callouts, tables, tags, and note properties.**

Select Plectics Alto Icons in Appearance settings. Its typography and component styling apply to existing notes; Style Settings exposes optional appearance controls. Typed Notes provides optional tag-family and display-title behaviour.

## Proposed registry entry

Historical destination: append one object to `community-css-themes.json`. This is valid JSON, and the screenshot is included on this branch. The current directory manages the registry entry.

```json
{
  "name": "Plectics Alto Icons",
  "author": "1800MIRACLE",
  "repo": "1800MIRACLE/obsidian.themes.plectics-alto-icons",
  "screenshot": "screenshots/preview.png",
  "modes": ["dark", "light"]
}
```

## Readiness and remaining work

The imported branch contains root `theme.css`, `manifest.json`, and GPL-3.0 `LICENSE`. The manifest declares version `0.1.0` and minimum Obsidian `1.6.0`. Both light and dark CSS are present. This verifies packaging, not compatibility with every supported version or platform.

Before submitting:

1. Merge the reviewed branch into the public default branch, including the usage README and a representative screenshot. Verify the proposed screenshot depicts this theme and has a 16:9 aspect ratio; 512 × 288 is recommended by the [official sample theme](https://github.com/obsidianmd/obsidian-sample-theme#add-a-screenshot-thumbnail).
2. Publish a GitHub release tagged exactly `0.1.0`, with `manifest.json` and `theme.css` as individual attachments. The destination repository had no releases when checked. A source archive or download ZIP alone does not meet this requirement.
3. Run the current theme review/lint checks and test the release in Obsidian, including both modes and the stated minimum app version. This preparation did not perform that runtime validation. Review the [theme guidelines](https://docs.obsidian.md/Themes/App%20themes/Theme%20guidelines) and [developer policies](https://docs.obsidian.md/Developer%20policies) before making the maintainer attestations.
4. Verify the final distributed assets and notices together. `NOTICE.md` and `licences/{OFL-EBGaramond.txt,OFL-Archivo.txt,NimbusSans-COPYING.txt,NimbusSans-LICENSE.txt}` are present. The notice links the font sources and build scripts in the companion `1800MIRACLE/obsidian.themes.plectics-alto` repository. Nimbus Sans is covered by AGPL-3.0; its written font exception specifically concerns PostScript/PDF. Keep the corresponding source and build scripts publicly available in the companion repository, and verify release distribution obligations rather than treating the theme's GPL file as a replacement for font licences. The notice also identifies Lucide ISC/Feather MIT assets; confirm applicable notices for the selected icons. This is an inventory, not a completed legal review.

The icon notice identifies Farm-Fresh v3.92 by FatCow under CC BY 3.0 US, including modified compositions. Confirm the required attribution and modification notices accompany the final CSS distribution; no independent provenance audit was performed.

The shipped-font inventory distinguishes embedded Alto Garamond Condensed, Archivo, and Nimbus Sans from fonts merely named in CSS fallback stacks. A named commercial font is not, by itself, evidence that its font data is distributed. Do not certify all assets solely from that distinction.

## Historical PR text

Title: `Add theme: Plectics Alto Icons`

The following body follows the former template's structure. Checkboxes intentionally do not attest to work that remains unverified.

```markdown
# I am submitting a new Community Theme

## Repo URL

https://github.com/1800MIRACLE/obsidian.themes.plectics-alto-icons

Plectics Alto Icons is a light and dark theme for research notes. It combines colour icons, serif typography and compact desktop-style controls with styling for mathematical callouts, tables, tags, and note properties. Select it in Appearance settings; optional Style Settings controls adjust the appearance.

## Theme checklist

- [x] Root manifest.json and theme.css are included in the proposed implementation.
- [x] A 16:9 preview image is available at screenshots/preview.png.
- [x] The declared modes are dark and light.
- [ ] The maintainer has assessed compliance with Obsidian developer policies.
- [ ] The maintainer has completed the theme-guideline self-review.
- [x] A root LICENSE file is included.
- [ ] Third-party asset licences, source availability, and attribution have been checked for the final distribution.
```

## Format references

- [Historical official theme template](https://github.com/obsidianmd/obsidian-releases/blob/c884be96dd43af0bafa7c1a1d80e767d03f2b6ec/.github/PULL_REQUEST_TEMPLATE/theme.md).
- [Accepted Brutalist addition, PR #8754 recorded in the merge commit](https://github.com/obsidianmd/obsidian-releases/commit/030e25677cf9ca3ddd255115ebaac538af3b3232): one registry object with name, author, repository, screenshot, and modes. The current PR endpoint was unavailable; the accepted commit was inspected directly.

No upstream PR, account change, release publication, exhaustive security review, or legal clearance was performed.

