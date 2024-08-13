import unittest
from src.scraper import WebScraper

class TestWebScraper(unittest.TestCase):
    def setUp(self):
        self.scraper = WebScraper('http://example.com')

    def test_fetch_content(self):
        from unittest.mock import patch
        with patch('requests.get') as mocked_get:
            mocked_get.return_value.status_code = 200
            mocked_get.return_value.content = b'<html></html>'
            content = self.scraper.fetch_content()
            self.assertEqual(content, b'<html></html>')

    def test_parse_content(self):
        content = '<html><body><div class="item-class"><span class="title-class">Item 1</span><span class="price-class">$10</span></div></body></html>'
        data = self.scraper.parse_content(content)
        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['title'], 'Item 1')
        self.assertEqual(data[0]['price'], '$10')

if __name__ == '__main__':
    unittest.main()