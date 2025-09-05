import sys
import os
import xml.etree.ElementTree as ET


def get_leaves(node, leaves):
    if len(node) == 0:
        leaves.append(node)
        return
    for child in node:
        get_leaves(child, leaves)
    

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
        tree = ET.parse(os.path.join(directory, name + ".xml"))
        root = tree.getroot()
        leaves = []
        get_leaves(root, leaves)
        print(leaves)

if __name__ == "__main__":
    main()