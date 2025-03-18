import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType

class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )
class TestingMarkdown(unittest.TestCase):
    def test_finding_markdown_types(self):
        # Create a block for each type
        '''
    paragraph
    heading
    code
    quote
    unordered_list
    ordered_list
'''
        para_block = '''Grate
Great
Hello'''
        self.assertEqual(block_to_block_type(para_block), BlockType.PARAGRAPH)

        head_block = '''### Grrr 
#### Healthy
### Normal'''

        self.assertEqual(block_to_block_type(head_block), BlockType.HEADING)

        code_block = '''```Codes stuffs
More codes stuffs
and even more code stuffs```'''
        
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)

        quote_block = '''>Hello
> More
> Dead'''

        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)

        unordered_list = '''- Enray
- Booth red
- Embrace Exponentials'''

        self.assertEqual(block_to_block_type(unordered_list), BlockType.UNORDERED_LIST)

        ordered_list = '''1. Hello world
2. LLMS are too good
3. Cursor is cool'''

        self.assertEqual(block_to_block_type(ordered_list), BlockType.ORDERED_LIST)