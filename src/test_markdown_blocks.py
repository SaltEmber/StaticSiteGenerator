import unittest

from markdown_blocks import markdown_to_blocks, block_to_block_type, BlockType, markdown_to_html_node

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

class TestingMarkdownToHTMLNode(unittest.TestCase):
        def test_paragraphs(self):
                md = """This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(
                html,
                "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
                )

        def test_codeblock(self):
                md = """```
This is text that _should_ remain
the **same** even with inline stuff
                ```
                """

                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(
                        html,
                        "<div><pre><code>\nThis is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
                )
        def test_headings(self):
                md = '### Heading3'

                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(
                        html,
                        "<div><h3>Heading3</h3></div>"
                )
        def test_unordered_list(self):
                md = """- This
- is
- an unordered list"""

                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(
                        html,
                        "<div><ul><li>This</li><li>is</li><li>an unordered list</li></ul></div>"
                )
        def test_ordered_list(self):
                md = """1. This
2. is an
3. ordered list"""

                node = markdown_to_html_node(md)
                html = node.to_html()
                self.assertEqual(
                        html,
                        "<div><ol><li>This</li><li>is an</li><li>ordered list</li></ol></div>"
                )