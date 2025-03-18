import unittest

from splitnodes import split_nodes_delimiter, split_nodes_image, split_nodes_link, text_to_textnodes
from textnode import TextNode, TextType

class TestSplitNodes(unittest.TestCase):
    def test_split_nodes(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes[1].text, "code block")
        self.assertEqual(new_nodes[1].text_type, TextType.CODE)

        node2 = TextNode("This is text with a 'code block word", TextType.TEXT)
        self.assertRaises(Exception,split_nodes_delimiter([node2], "`", TextType.CODE))

class TestSplitNodesImage(unittest.TestCase):
    def test_split_images(self):
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.TEXT,
        )
        new_nodes = split_nodes_image([node])
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
                TextNode(" and another ", TextType.TEXT),
                TextNode(
                    "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
                ),
            ],
            new_nodes,
        )

    def empty_node_text_image(self):
        node = TextNode("Very much much", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertListEqual(split_nodes_link([node, node2]), [TextNode("Very much much", TextType.TEXT)])
    def no_link_text_image(self):
        node = TextNode("Hello what is it if not a box?", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), TextNode("Hello what is it if not a box?", TextType.TEXT))

class TestSplitNodesLink(unittest.TestCase):
    def test_split_nodes_link(self):
        node = TextNode(
            "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
            TextType.TEXT
        )
        new_nodes = split_nodes_link([node])
        self.assertListEqual(
            [
                    TextNode("This is text with a link ", TextType.TEXT),
                    TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
                    TextNode(" and ", TextType.TEXT),
                    TextNode(
                        "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
                    ),
                ], new_nodes
        )

    def empty_node_text_link(self):
        node = TextNode("Very much much", TextType.TEXT)
        node2 = TextNode("", TextType.TEXT)
        self.assertListEqual(split_nodes_link([node, node2]), [TextNode("Very much much", TextType.TEXT)])
    def no_link_text_node(self):
        node = TextNode("Hello what is it if not a box?", TextType.TEXT)
        self.assertEqual(split_nodes_link([node]), TextNode("Hello what is it if not a box?", TextType.TEXT))

class TestTextToTextnodes(unittest.TestCase):
    def testing_default(self):
        text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        new_nodes = text_to_textnodes(text)
        self.assertListEqual(new_nodes,
        [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev")
        ])
