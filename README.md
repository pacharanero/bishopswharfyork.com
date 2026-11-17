# bishopswharfyork.com

Static site for [bishopswharfyork.com](https://bishopswharfyork.com/), built with [Zensical](https://zensical.org/) using the Modern theme (light scheme by default, with a dark-mode toggle). Built by Marcus Baw, as a free service to the community.

## Domains

Bishops Wharf related domains are controlled by Marcus Baw via Cloudflare.

cherryhillyork.com -> 301 redirect via Cloudflare Rules to bishopswharfyork.com
posterncloseyork.com -> 301 redirect via Cloudflare Rules to bishopswharfyork.com
posterncloseyork.co.uk -> 301 redirect via Cloudflare Rules to bishopswharfyork.com

## Content

The current downloadable information booklet is the August 2026 edition. Most HTML pages retain wording from the previous site; the safety page identifies the superseded fire guidance and directs residents to the current booklet and the managing agent's fire-safety leaflet.

Markdown pages live in `docs/`, images and PDFs in `docs/assets/`.

Navigation order is defined in `mkdocs.yml`.

The original scraped HTML and images are preserved for posterity in
`original-site-archive/`.

The previous booklet is retained unchanged at `original-site-archive/Bishops Wharf leaflet.pdf`. Keep historical booklets outside `docs/` so obsolete guidance is not published as current site content. The current booklet uses the stable URL `assets/bishops-wharf-leaflet.pdf` so existing download links continue to work.

## Local development

```bash
./s/dev
```

This creates a `.venv/` on first run, installs `zensical`, and serves the site at <http://127.0.0.1:8000/> with live reload.

To build a static copy into `site/`:

```bash
source .venv/bin/activate
zensical build --clean
python -m unittest discover -s tests -v
```

## Deployment

`.github/workflows/deploy-docs-to-ghpages.yml` builds and checks local links and navigation on pull requests and pushes to `main`, and audits workflow security with Zizmor. Only `main` deploys to GitHub Pages; pull requests receive no deployment permissions.
