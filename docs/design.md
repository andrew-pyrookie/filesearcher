Using >>> $ echo -e "\U0001F50D Search" - magnifying lens icon

>>> (filesearcher/OS) $ "command"     # Search the whole Operating system
>>> (filesearcher/Dir) $ "command"    # Expected directory name, to look files in. 


>>> (filesearcher/Dir) $ exit         # Exit the script

# File Searcher Design

## Overview
The File Searcher is a Python script designed to search for files based on specific criteria. It provides functionality to search by file name, file extension, file content, file size, and modification time.

## Architecture
The script follows a modular architecture with the following components:
- `file_filter.py`: Implements file filtering functions.
- `search_engine.py`: Implements file search functionality.
- `main.py`: The main entry point of the script.

## File Search Process
The file search process involves the following steps:
1. User provides the search criteria.
2. The search engine module scans the specified directory or the entire operating system based on user input.
3. The search engine applies the specified filters to match the search criteria.
4. The search engine returns the list of matching files.

## Dependencies
The script relies on the following Python libraries:
- `os`: For directory traversal and file-related operations.
- `colorama`: For colored output.

