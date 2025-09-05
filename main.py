import sys
import os
import Node as XMLTree




class Node:

    def __init__(self):
        self.children = []

    def read_metadata(self, data):
        print(data)


def main():
    directory = ""
    file_names = []
    node = XMLTree

    if len(sys.argv) == 2 and os.path.isdir(sys.argv[1]):
        directory = sys.argv[1]
    else:
        raise TypeError("no directory given")
    
    all_files = os.listdir(directory)
    
    for i in range(len(all_files)):
        all_files[i] = all_files[i][:-4]
    file_names = set(all_files)
    
    for name in file_names:
        with open(os.path.join(directory, name + ".xml")) as file:
            xml_file = file.read()
            node.read_metadata(xml_file)
            


if __name__ == "__main__":
    main()