import os
import shutil
import sys
from textnode import *
from copystatic import *
from page_generator import *

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    print("Deleting the public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to a public directory...")
    copy_static(dir_path_static, dir_path_public)

    print("Generating the page...")
    process_all_markdown_files(dir_path_content, template_path, dir_path_public, basepath)


main()
