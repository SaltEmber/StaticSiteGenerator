import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
    def test_leaf_to_html_attrs(self):
        node = LeafNode("h1", "Good morning, world.", {"href": "https://google.com", "target": "_blank"})
        self.assertEqual(node.to_html(), '<h1 href="https://google.com" target="_blank">Good morning, world.</h1>')
    def test_output_raw_string(self):
        node = LeafNode(None, "Good morning, world.")
        self.assertEqual(node.to_html(), "Good morning, world.")
