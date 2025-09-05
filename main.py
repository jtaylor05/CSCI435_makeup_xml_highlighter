import sys
import os
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw, ImageFont


def get_leaves(node, leaves):
    if len(node) == 0:
        leaves.append(node)
        return
    for child in node:
        get_leaves(child, leaves)

def draw_highlights(directory, file_name, save_directory = ""):
    tree = ET.parse(os.path.join(directory, file_name) + ".xml")
    root = tree.getroot()
    leaves = []
    get_leaves(root, leaves)
    
    with Image.open(os.path.join(directory, file_name) + ".png").convert("RGBA") as base:
        d = ImageDraw.Draw(base)
        
        for leaf in leaves:
            bounds = leaf.attrib["bounds"]
            print(leaf.attrib["class"])
            bounds = bounds.replace("][", ",")[1:-1].split(",")
            for i in range(len(bounds)):
                bounds[i] = int(bounds[i])
            
            d.rectangle(bounds, outline = (255, 255, 40), width = 4)

        base.save(os.path.join(save_directory, file_name) + ".highlight.png")

def main():
    directory = ""
    file_names = []

    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        directory = sys.argv[1]
    else:
        raise TypeError("no directory given")
    
    all_files = os.listdir(directory)
    
    for i in range(len(all_files)):
        all_files[i] = all_files[i][:-4]
    file_names = list(set(all_files))
    for name in file_names:
        draw_highlights(directory, name)
    

if __name__ == "__main__":
    main()