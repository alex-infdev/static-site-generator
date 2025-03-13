import os
import shutil
from textnode import *
from copystatic import *

dir_path_static = "./static"
dir_path_public = "./public"

def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    
    print("Copying static files to public directory...")
    copy_static(dir_path_static, dir_path_public)

if __name__ == "__main__":
    main()