import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        # Testing whether a single variable change makes them differ
        node3 = TextNode("This is not a text node", TextType.BOLD)
        node4 = TextNode("This is a text node", TextType.NORMAL)
        node5 = TextNode("This is a text node", TextType.BOLD, "https://boot.dev")
        self.assertEqual(node, node2)
        # Testing for the single varaible alteration cases
        self.assertNotEqual(node, node3)
        self.assertNotEqual(node, node4)
        self.assertNotEqual(node, node5)

if __name__ == "__main__":
    unittest.main()
