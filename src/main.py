import os
import shutil
from textnode import TextNode
from htmlnode import ParentNode, HTMLNode, LeafNode

def generate_output(source, destination):
    if not os.path.exists(source):
        raise ValueError(f"Source path doesn't exist: {source}")
    if not os.path.exists(destination):
        raise ValueError(f"Destination path doesn't exist: {destination}")
    final_destination = os.path.join(destination, 'public')
    if os.path.exists(final_destination):
        shutil.rmtree(final_destination)
    os.mkdir(final_destination)
    copy_paste(source, final_destination)

def copy_paste(source, destination):
    files = os.listdir(source)
    for file in files:
        new_source = os.path.join(source, file)
        new_destination = os.path.join(destination, file)
        if os.path.isfile(new_source):
            shutil.copy(new_source, new_destination)
        else:
            os.mkdir(new_destination)
            copy_paste(new_source, new_destination)





def main():
    source  = "/home/deusvitae/workspace/github.com/SumDeusVitae/static_site_generator/static"
    destination = "/home/deusvitae/workspace/github.com/SumDeusVitae/static_site_generator"
    generate_output(source, destination)

main()

