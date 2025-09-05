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

def draw_dashed_rectangle(d : Image, bounds = [0,0,0,0], line_fill=(255, 255, 40), dash_length = 5, gap = 10, w = 15):
    for x in range(bounds[0], bounds[2], dash_length + gap):
        d.line([(x, bounds[1]), (x + dash_length, bounds[1])],fill = line_fill, width = w) 
    for x in range(bounds[0], bounds[2], dash_length + gap):
        d.line([(x, bounds[3]), (x + dash_length, bounds[3])],fill = line_fill, width = w) 
    for y in range(bounds[1], bounds[3], dash_length + gap):
        d.line([(bounds[0], y), (bounds[0], y + dash_length)],fill = line_fill, width = w) 
    for y in range(bounds[1], bounds[3], dash_length + gap):
        d.line([(bounds[2], y), (bounds[2], y + dash_length)],fill = line_fill, width = w) 

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
            bounds = [int(x) for x in bounds]
            draw_dashed_rectangle(d, bounds)

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