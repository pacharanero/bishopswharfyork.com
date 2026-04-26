# bishopswharfyork.com

Static site for [bishopswharfyork.com](https://bishopswharfyork.com/), built with
[Zensical](https://zensical.org/) using the Modern theme (light scheme by default,
with a dark-mode toggle).

## What this is

A straight-up replacement for the existing, 1990s-era site, with the wording kept
**verbatim**. The aim of this first pass is purely a visual and structural upgrade
plus search out of the box. Copy changes are a separate, later job.

## Content

Markdown pages live in `docs/`, images and PDFs in `docs/assets/`. Navigation order
is defined in `mkdocs.yml`.

The original scraped HTML and images are preserved for posterity in
`original-site-archive/`.

## Local development

```bash
./s/dev
```

This creates a `.venv/` on first run, installs `zensical`, and serves the site
at <http://127.0.0.1:8000/> with live reload.

To build a static copy into `site/`:

```bash
source .venv/bin/activate
zensical build --clean
```

## Deployment

`.github/workflows/deploy-docs-to-ghpages.yml` builds on every push to `main` and
deploys to GitHub Pages.
