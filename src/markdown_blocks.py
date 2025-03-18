from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered list"
    ORDERED_LIST = "ordered_list"

def markdown_to_blocks(markdown):
    lines = markdown.split('\n\n')
    new_lines = []
    for line in lines:
        if line == "":
            continue
        new_lines.append(line.strip())
    return new_lines

def block_to_block_type(markdown_block):
    if len(re.findall(r'^#{1,7} *', markdown_block, re.MULTILINE)) == markdown_block.count('\n') + 1:
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

code_block = '''```Codes stuffs
More codes stuffs
and even more code stuffs```'''
print(block_to_block_type(code_block))