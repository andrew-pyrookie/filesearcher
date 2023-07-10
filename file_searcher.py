#!/usr/bin/env python3
import os
import colorama
import sys

def which_dir(path):
    if path.upper() == "OS" or path == "/":
        path = os.getcwd()
    else:
        path = os.path.abspath(path)
    return path

def byname(name, dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            if name == file:
                return os.path.join(root, file)
    return None

def by_extension(extension, dir):
    matching_files = []
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.endswith(extension):
                matching_files.append(os.path.join(root, file))
    return matching_files

def exit_program(input):
    if input.upper() == "EXIT":
        sys.exit()

def green_text(text):
    return colorama.Fore.GREEN + text + colorama.Fore.RESET

# Initialize colorama
colorama.init()

print("FILE SEARCHER")

if len(sys.argv) != 4:
    print("Usage: python file_searcher.py <directory> <name> <extension>")
    sys.exit(1)

path = which_dir(sys.argv[1])
name = sys.argv[2]
extension = sys.argv[3]

while True:
    if path == "":
        cmd = green_text(f">>> (fileSearcher) $ ")
    else:
        cmd = green_text(f">>> (fileSearcher/{path}) $ ")

    user_input = input(cmd)
    exit_program(user_input)

    path = which_dir(path + "/" + user_input)
    name_result = byname(name, path)
    extension_result = by_extension(extension, path)

    if name_result:
        print("Matching file found:")
        print(name_result)
    elif extension_result:
        print("Matching files found:")
        for file_path in extension_result:
            print(file_path)
    else:
        print("No matching file or files found.")
