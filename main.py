import sys
import os
import xml.etree.ElementTree as ET

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
        print(tree.getroot())

if __name__ == "__main__":
    main()