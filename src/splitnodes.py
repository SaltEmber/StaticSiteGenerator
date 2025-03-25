from doctest import Example
from textnode import TextNode, TextType
import re


'''
    return nodes objects split from given nodes with proper TextType

    input: nodes, delimiter (used to find the target text_type), text_type (the target of search)

    -only attempt to work on text_type TextType.TEXT, if not add to list as is
        -conditional ensure isinstance(TextType.TEXT)
'''


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        odd = True
        if node.text_type == TextType.TEXT:
            text = node.text.split(delimiter)
            if not text.count(delimiter) % 2 == 0:
                raise Exception("Missing closing delimiter")
            for interval in text:
                if odd:
                    new_nodes.append(TextNode(interval, TextType.TEXT))
                else:
                    new_nodes.append(TextNode(interval, text_type))
                odd = not odd
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT),]
    type_delim = {
        TextType.BOLD: TextType.BOLD.value,
        TextType.ITALIC: TextType.ITALIC.value,
        TextType.CODE: TextType.CODE.value
    }
    for type, delim in type_delim.items():
        nodes = split_nodes_delimiter(nodes, delim, type)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\]]*)\]\(([^\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\]]*)\]\(([^\]]*)\)", text)

def split_nodes_image(old_nodes):
    '''
        input: old TextNodes which maybe contain text
        return: list of TextNodes according to their types

        separate elements into regular text and images:
            - repeatedly split the text up using the pairs found using extract_mardown_images

        working on an Example
        text = "helehelheehl, {allat} is very funny is it not? {allat} {allat} ekekekekek I would find nothing funnier"

        split for first {allat}:
            ["helehelheehl", "", "is very funny is it not? {allat} {allat} ekekekekek I would find nothing funnier"]
            okay now we can just keep spliting it and when we reach an empty character we can just create a new link node
    '''
    new_nodes = []
    for node in old_nodes:
        if not node:
            continue
        text = [node.text]
        if not text:
            continue
        # This returns an empty list if there is no image
        list_tuples = extract_markdown_images(text[0])
        # Alter text to turn it into a list, where all of the image characters are accounted for (in terms of being an empty spot)
        new_text = []
        
        if not list_tuples:
            new_nodes.append(node)
            continue

        for elem in list_tuples:
            alt_text, image_link = elem
            text = text[len(text) - 1].split(f"![{alt_text}]({image_link})", maxsplit=1)
            new_text.append(text[0])
        new_text.append(text[1])
    #     Obtain the split, if split == '' then append to list image_link
        index_counter = 0
        for section in new_text:
            if not section == "":
                new_nodes.append(TextNode(section, TextType.TEXT))
            if len(list_tuples) > index_counter:
                new_nodes.append(TextNode(list_tuples[index_counter][0], TextType.IMAGE, list_tuples[index_counter][1]))
            index_counter += 1
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if not node:
            continue
        text = [node.text]
        if not text:
            continue
        # This returns an empty list if there is no image
        list_tuples = extract_markdown_links(text[0])
        # Alter text to turn it into a list, where all of the image characters are accounted for (in terms of being an empty spot)
        new_text = []
        '''
            input: list_tuples(a list containing pairs we use to match a split with)
            
            return: list(str) containing no links
        '''
        if not list_tuples:
            new_nodes.append(node)
            continue
        for elem in list_tuples:
            alt_text, link = elem
            text = text[len(text) - 1].split(f"[{alt_text}]({link})", maxsplit=1)
            new_text.append(text[0])
        new_text.append(text[1])
    #     Obtain the split, if split == '' then append to list image_link
        index_counter = 0
        for section in new_text:
            if not section == "": 
                new_nodes.append(TextNode(section, TextType.TEXT))
            if len(list_tuples) > index_counter:
                new_nodes.append(TextNode(list_tuples[index_counter][0], TextType.LINK, list_tuples[index_counter][1]))
            index_counter += 1
    return new_nodes
