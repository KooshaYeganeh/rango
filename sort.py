import glob
import os
import sys


directory_path = sys.argv[2]

def sort_files():
    # Specify the directory path where the files are located
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
    return "all Files in Directory Sorted [ OK ]"
