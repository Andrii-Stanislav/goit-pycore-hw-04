import pathlib
import os

def get_cats_info(absolute_path):
    if not os.path.exists(absolute_path):
        return 'File does not exist'
    
 
    cats_info = []
    with open(pathlib.Path(absolute_path)) as file:
        for line in file:
            id, name, age = line.strip().split(',')
            cat_info = {
                'id': id,
                'name': name,
                'age': age
            }
            
            cats_info.append(cat_info)

    return cats_info
