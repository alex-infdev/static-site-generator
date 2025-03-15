import os
from markdown_blocks import *

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("#"):
            return line[1:].strip()
        
    raise Exception("No H1 header found.")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    from_file = open(from_path, "r")
    markdown_content = from_file.read()
    from_file.close()

    template_file = open(template_path, "r")
    template = template_file.read()
    template_file.close()

    node = markdown_to_html_node(markdown_content)
    html = node.to_html()

    title = extract_title(markdown_content)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)

    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    to_file = open(dest_path, "w")
    to_file.write(template)
    to_file.close()

def process_all_markdown_files(content_dir, template_path, public_dir):
    for root, dirs, files in os.walk(content_dir):
        for file in files:
            if file.endswith(".md"):
                markdown_path = os.path.join(root, file)

                rel_path = os.path.relpath(root, content_dir)

                if file == "index.md":
                    dest_path = os.path.join(public_dir, rel_path, "index.html")
                else:
                    file_name = file[:-3]
                    dest_path = os.path.join(public_dir, rel_path, file_name, "index.html")
                generate_page(markdown_path, template_path, dest_path)