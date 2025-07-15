from csv import reader
from os import walk,path
import pygame

def import_csv_layout(path):
    terrain_map=[]
    with open(path) as level_map:
        layout=reader(level_map,delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
    
def import_folder(folder_path):
    surface_list = []
    
    absolute_folder_path = path.abspath(folder_path)

    for _, __, img_files in walk(absolute_folder_path):
        for image in img_files:
            full_path = path.join(absolute_folder_path, image)
            try:
                image_surf = pygame.image.load(full_path).convert_alpha()
                surface_list.append(image_surf)
            except pygame.error as e:
                print(f"Error loading image at {full_path}: {e}") 

    return surface_list