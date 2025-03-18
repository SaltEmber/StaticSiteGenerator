import unittest

from htmlnode import LeafNode
from textnode import TextNode, TextType
from textnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        # Testing whether a single variable change makes them differ
        node3 = TextNode("This is not a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.TEXT)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node, node2)
        # Testing for the single varaible alteration cases
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)

    def test_text_to_html_node(self):
        # Raw text
        node = TextNode("This is a raw text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, None)

        # Regular TextNode
        node1 = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node1)
        self.assertEqual(html_node.tag, None)

        # Bold TextNode
        node2 = TextNode("This is a bolded node", TextType.BOLD)
        html_node = text_node_to_html_node(node2)
        self.assertEqual(html_node.tag, "b")

        # Italic TextNode
        node3 = TextNode("This is an italic textnode", TextType.ITALIC)
        html_node = text_node_to_html_node(node3)
        self.assertEqual(html_node.tag, "i")
        # Code TextNode
        node4 = TextNode("This is a code textnode", TextType.CODE)
        html_node = text_node_to_html_node(node4)
        self.assertEqual(html_node.tag, "code")
        # Link TextNode
        node5 = TextNode("This is a link test node", TextType.LINK, "https://boot.dev")
        html_node = text_node_to_html_node(node5)
        self.assertEqual(html_node.tag, "a")
        self.assertEqual(html_node.props, {"href": "https://boot.dev"})
        # Image TextNode
        node6 = TextNode("This is some alt text", TextType.IMAGE, "https://boot.dev")
        html_node = text_node_to_html_node(node6)
        self.assertEqual(html_node.tag, "img")
        self.assertEqual(html_node.props["src"], "https://boot.dev")
        self.assertEqual(html_node.props["alt"], "This is some alt text")



if __name__ == "__main__":
    unittest.main()
