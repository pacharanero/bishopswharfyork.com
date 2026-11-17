"""Check navigation and local links after `zensical build --clean`."""

from html.parser import HTMLParser
import hashlib
from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "site"


class LocalLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        for name, value in attrs:
            if name in {"href", "src"} and value:
                url = urlsplit(value)
                if not url.scheme and not url.netloc and url.path:
                    self.links.append(unquote(url.path))


class SiteTests(unittest.TestCase):
    def test_navigation_lists_every_page(self):
        config = (ROOT / "mkdocs.yml").read_text()
        # This site's nav contains plain, unquoted Markdown paths.
        listed = set(re.findall(r"^\s+- [^\n]+:\s+([^\s]+\.md)\s*$", config, re.M))
        pages = {
            str(path.relative_to(ROOT / "docs"))
            for path in (ROOT / "docs").rglob("*.md")
        }
        self.assertEqual(listed, pages)

    def test_built_local_links_exist(self):
        self.assertTrue((SITE / "index.html").is_file(), "Run zensical build --clean first")
        for page in SITE.rglob("*.html"):
            parser = LocalLinks()
            parser.feed(page.read_text())
            for link in parser.links:
                base = SITE if link.startswith("/") else page.parent
                target = base / link.lstrip("/")
                with self.subTest(page=str(page.relative_to(SITE)), link=link):
                    self.assertTrue(target.exists(), f"Missing local target: {target}")

    def test_current_booklet_is_published(self):
        source = ROOT / "docs/assets/bishops-wharf-leaflet.pdf"
        published = SITE / "assets/bishops-wharf-leaflet.pdf"
        self.assertEqual(source.read_bytes(), published.read_bytes())

    def test_original_booklet_is_preserved(self):
        archived = ROOT / "original-site-archive/Bishops Wharf leaflet.pdf"
        self.assertEqual(
            hashlib.sha256(archived.read_bytes()).hexdigest(),
            "be144530d5f2e48abf1efb2688b823a2443ef3c1a34cf091f521106e57a0cb31",
        )


class LocalLinksTests(unittest.TestCase):
    def test_ignores_external_links_and_fragment_only_links(self):
        parser = LocalLinks()
        parser.feed('<a href="https://example.com/">External</a><a href="#top">Top</a>')
        parser.feed('<a href="//example.com/">External</a><a href="mailto:a@b.com">Email</a>')
        self.assertEqual(parser.links, [])

    def test_decodes_local_paths_and_discards_queries_and_fragments(self):
        parser = LocalLinks()
        parser.feed('<a href="assets/old%20booklet.pdf?download=1#page=2">PDF</a>')
        parser.feed('<img src="/assets/photo.png">')
        self.assertEqual(parser.links, ["assets/old booklet.pdf", "/assets/photo.png"])


if __name__ == "__main__":
    unittest.main()
