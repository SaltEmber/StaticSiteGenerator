import shutil
import os
import re
import sys
from textnode import TextNode, TextType
from markdown_blocks import markdown_to_html_node

def main():
    BASEPATH = sys.argv[1] if len(sys.argv) > 1 else "/"
    
    move_files('static', 'docs')
    generate_pages_recursive("content", "template.html", "docs", BASEPATH)
def move_files(source_path, dest_path):
    '''
        Inputs: 
            -source_path the current working path within the static file
            -dest_path the current working path within the dest_path

        - for the given directory (within the source_path) check if listdir element is a file
        - if the element is a file, then copy the file into the same area but inside the dest_file path
        - if the element is not a file, create a new directory in the dest_path then recurse within it

    '''
    if dest_path == 'docs':
        try:
            shutil.rmtree('docs')
        except:
            pass
        os.mkdir('docs')

    for elem in os.listdir(source_path):
        new_path = f'{source_path}/{elem}'
        if os.path.isfile(new_path):
            shutil.copy(new_path, dest_path)
        else:
            os.mkdir(f'{dest_path}/{elem}')
            move_files(new_path, f'{dest_path}/{elem}')

def extract_title(markdown):
    block_html = markdown_to_html_node(markdown)
    headings = re.findall(r'<h1>([\s\S]*)<\/h1>', block_html.to_html())
    if not headings:
        raise Exception("There is no heading.")
    return headings 

def generate_page(from_path, template_path, dest_path, BASEPATH):
    # Printing required message
    print(f"Generating page from {from_path} to {dest_path} using template_path")
    # Opening the markdown source file and template file to take their contents as values
    with open(from_path, 'r') as file:
        md_file = file.read()
    with open(template_path, 'r') as file:
        template_file = file.read()
    # Obtaining html node for the markdown page
    html = markdown_to_html_node(md_file).to_html()
    title = extract_title(md_file)[0]
    new_file = template_file.replace("{{ Title }}", title).replace('{{ Content }}', html)
    # Set BASEPATH
    new_file = new_file.replace('href="/',f'href="{BASEPATH}').replace('src="/',f'src="{BASEPATH}')

    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    
    with open(dest_path, 'w') as file:
        file.write(new_file)
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, BASEPATH):
    '''
        Input:
            -dir_path_content: the path to the source content
            -template_path: should remain constant (the path of our template used to generate the page)
            -dest_dir_path: the path to put the html of the content 

        -check scan through the directory 
        -check if element is a file
            -if it is then create a file with it
            -if it is not then make a new_directory and continue recursing through that path   
    '''
    for elem in os.listdir(dir_path_content):
        elem_path = os.path.join(dir_path_content, elem)
        new_path = os.path.join(dest_dir_path, elem)
        if os.path.isfile(elem_path):
            generate_page(elem_path, template_path, new_path.rstrip("md") + "html", BASEPATH)
            continue
        os.mkdir(os.path.join(dest_dir_path, elem))
        generate_pages_recursive(elem_path, template_path, new_path, BASEPATH)

if __name__ == "__main__":
    main()
