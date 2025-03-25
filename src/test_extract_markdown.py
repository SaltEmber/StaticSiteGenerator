import unittest

from splitnodes import extract_markdown_images, extract_markdown_links
from main import extract_title

class TestExtractMarkdownImages(unittest.TestCase):
    def testing_regex(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
        self.assertEqual(extract_markdown_images(text),[("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")])
    def testing_regex_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]
        self.assertEqual(extract_markdown_links(text), [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")])

    def testing_regex_with_brackets(self):
        text = "[Link to Wikipedia](https://en.wikipedia.org/wiki/Bracket_(disambiguation))"
        self.assertEqual(extract_markdown_links(text), [("Link to Wikipedia", "https://en.wikipedia.org/wiki/Bracket_(disambiguation)")])

class TestExtractTitle(unittest.TestCase):
    def test_single_word(self):
        self.assertEqual(extract_title("# Hello"), ["Hello"])
    def test_multi_word(self):
        self.assertEqual(extract_title("# Hello world"), ["Hello world"])
    def test_error_case(self):
        with self.assertRaises(Exception):
            extract_title("Hello world")