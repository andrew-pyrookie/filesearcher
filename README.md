#!/usr/bin/env python3

Make the script executable by changing its file permissions. 

chmod +x file_searcher.py

Add your script to a directory listed in the system's PATH environment variable. 
By doing this, you make the script accessible from anywhere on the system. 

You can either add the script to an existing directory already in the PATH or create a new directory for your custom scripts and add it to the PATH.

For example, you can create a directory named ~/scripts and add it to the PATH by adding the following line to your shell configuration file (e.g., .bashrc, .bash_profile, or .zshrc):

export PATH="$HOME/scripts:$PATH"

Save the file and run 'source  -/.bashrc'

# File Searcher

File Searcher is a Python script that allows you to search for files based on specific criteria such as file name, extension, content, size, and modification time.

## Features

- Search for files by name
- Filter files by extension
- Search files based on their content
- Filter files by size
- Search files by modification time

## Requirements

- Python 3.x

## Installation

1. Clone the repository or download the script files.
2. Install the required dependencies using the command: `pip install -r requirements.txt`

## Usage


- `<directory>`: The directory to search within. Use `OS` to search the entire operating system.
- `<name>`: The file name to search for.
- `<extension>`: The file extension to filter by.

Example usage:


This command will search for files with the name "myfile" and the extension ".txt" within the entire operating system.

## License

This project is licensed under the [MIT License](LICENSE).
