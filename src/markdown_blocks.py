from enum import Enum
import re

from htmlnode import ParentNode, LeafNode
from splitnodes import text_to_textnodes
from textnode import text_node_to_html_node

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered list"

def markdown_to_blocks(markdown):
    lines = markdown.split('\n\n')
    new_lines = []
    for line in lines:
        if line == "":
            continue
        new_lines.append(line.strip('\n '))
    return new_lines

def block_to_block_type(markdown_block):
    if re.findall(r'^#{1,6} *', markdown_block, re.MULTILINE):
        return BlockType.HEADING
    elif re.findall(r'^`{3}([\s\S]*)`{3}$', markdown_block):
        return BlockType.CODE
    elif len(re.findall(r'^- *', markdown_block, re.MULTILINE)) == markdown_block.count('\n') + 1:
        return BlockType.UNORDERED_LIST
    elif len(re.findall(r'^>', markdown_block, re.MULTILINE)) == markdown_block.count('\n') + 1:
        return BlockType.QUOTE
    # Producers new lines
    list_markdown_block = markdown_block.split('\n')
    for i in range(1, len(list_markdown_block) + 1):
        if not list_markdown_block[i-1].split()[0] == f'{i}.':
            return BlockType.PARAGRAPH
    return BlockType.ORDERED_LIST

def text_to_children(text):

    new_text = text.replace('\n', ' ')
    new_textnodes = text_to_textnodes(new_text)
    new_nodes = []
    for node in new_textnodes:
        new_nodes.append(text_node_to_html_node(node))
    return new_nodes

def block_to_html(block, block_type):
    match block_type:
        case BlockType.PARAGRAPH:
            children = text_to_children(block)
            return ParentNode('p', children)
        case BlockType.HEADING:
            new_text = block.split(" ", maxsplit=1)[1]
            children = text_to_children(new_text)
            return ParentNode(f'h{block.count("#")}', children)
        case BlockType.CODE:
            new_text = block.split("```")[1:-1]
            new_code = "".join(new_text)
            new_code = new_code.strip(' ')
            code = LeafNode('code', new_code) 
            return ParentNode('pre', [code])
        case BlockType.UNORDERED_LIST:
            nodes = []
            elements = re.findall(r'- (.*?)$', block, re.MULTILINE)
            for elem in elements:
                children = text_to_children(elem)
                nodes.append(ParentNode('li', children))
            return ParentNode('ul', nodes)
        case BlockType.ORDERED_LIST:
            nodes = []
            for segment in block.split('\n'): 
                new_text = segment.split(' ', maxsplit=1)[1]
                children = text_to_children(new_text)
                nodes.append(ParentNode('li', children))
            return ParentNode('ol', nodes)
        case BlockType.QUOTE:
            new_text = block.split(" ", maxsplit=1)[1]
            children = text_to_children(new_text)
            return ParentNode('blockquote', children) 
            
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    html_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        html_blocks.append(block_to_html(block, block_type))

    return ParentNode('div', html_blocks)

