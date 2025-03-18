from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    # "Text"
    TEXT = "text"
    # "**Bold text**"
    BOLD = "**"
    #  "_Italic text_"
    ITALIC = "_"
    # "`Code text`"
    CODE = "`"
    # "[anchor text](url)"
    LINK = "link"
    # "![alt text](url)"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url
    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url
    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type.value}, {self.url})'

def text_node_to_html_node(text_node):
    node_text_type = text_node.text_type
    if not isinstance(node_text_type, TextType):
        raise Exception("Text Node TextType is not an instance of enum TextType")
    if node_text_type is TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif node_text_type is TextType.BOLD:
        return LeafNode("b", text_node.text)
    elif node_text_type is TextType.ITALIC:
        return LeafNode("i", text_node.text)
    elif node_text_type is TextType.CODE:
        return LeafNode("code", text_node.text)
    elif node_text_type is TextType.LINK:
        return LeafNode("a", text_node.text, n_props={"href": text_node.url})
    elif node_text_type is TextType.IMAGE:
        return LeafNode("img","",n_props={"src": text_node.url, "alt":text_node.text})
