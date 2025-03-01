import pathlib
import colorama
import os

def display_dir(absolute_path, level=0):
    if not os.path.exists(absolute_path):
        return print(f'File {absolute_path} does not exist')
    
    if not os.path.isdir(absolute_path):
        return print(f'Path {absolute_path} is not a directory')
    
    path = pathlib.Path(absolute_path)
    for item in path.iterdir():
        if item.is_file():
            print(colorama.Fore.GREEN + f'{"   " * level}{item.name}')
        else:
            print(colorama.Fore.BLUE + f'{"   " * level}{item.name}/')
            display_dir(item, level + 1)

    return