# bishopswharfyork.com

Static site for [bishopswharfyork.com](https://bishopswharfyork.com/), built with [Zensical](https://zensical.org/) using the Modern theme (light scheme by default, with a dark-mode toggle). Built by Marcus Baw, as a free service to the community.

## Domains

Bishops Wharf related domains are controlled by Marcus Baw via Cloudflare.

cherryhillyork.com -> 301 redirect via Cloudflare Rules to bishopswharfyork.com
posterncloseyork.com -> 301 redirect via Cloudflare Rules to bishopswharfyork.com
posterncloseyork.co.uk -> 301 redirect via Cloudflare Rules to bishopswharfyork.com

## Content

Content wording is unaltered from the previous site. The aim of this first pass is purely a visual and structural upgrade plus adding search.

Copy changes are a separate, later job.

Markdown pages live in `docs/`, images and PDFs in `docs/assets/`.

Navigation order is defined in `mkdocs.yml`.

The original scraped HTML and images are preserved for posterity in
`original-site-archive/`.

## Local development

```bash
./s/dev
```

This creates a `.venv/` on first run, installs `zensical`, and serves the site at <http://127.0.0.1:8000/> with live reload.

To build a static copy into `site/`:

```bash
source .venv/bin/activate
zensical build --clean
```

## Deployment

`.github/workflows/deploy-docs-to-ghpages.yml` builds on every push to `main` and deploys to GitHub Pages.
