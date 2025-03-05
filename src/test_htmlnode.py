import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        HTMLNode1 = HTMLNode("p", "This is the value of the node", None, {"href": "values", "target": "somewhere"})
        HTMLNode2 = HTMLNode("h1", "This is the text within my header.", None, {"href": "https://www.google.com", "target": "_blank"})
        self.assertEqual(str(HTMLNode1), "HTMLNode(p, This is the value of the node, None, {'href': 'values', 'target': 'somewhere'})")
        self.assertEqual(HTMLNode1.props_to_html(), ' href="values" target="somewhere"')
        self.assertEqual(HTMLNode2.props_to_html(), ' href="https://www.google.com" target="_blank"')
