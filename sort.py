#!/usr/bin/python3

import glob
import os
import sys

def sort_files(directory_path):
    # Use glob to find all files in the directory
    files = glob.glob(os.path.join(directory_path, "*"))

    # Sort files by their extension
    files.sort(key=lambda x: os.path.splitext(x)[1])

    # Iterate over the sorted files
    for file in files:
        # Get the file extension
        _, extension = os.path.splitext(file)

        # Print the file name and extension
        print(f"File: {file} \t Type: {extension}")
    return "All Files in Directory Sorted [ OK ]"

# Do not execute sorting when this file is imported
if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        print(sort_files(directory_path))
    else:
        print("No directory path provided.")

