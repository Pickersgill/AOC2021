import numpy as np
from PIL import Image
import sys
from grid import Point, Grid

def draw_img(arr):
    color_grid = arr * 255
    img = Image.fromarray(np.uint8(color_grid))
    img.show()
    

def decode(file_loc):
    with open(file_loc) as src:
        text = src.read()
    
        lines = text.splitlines()
        key = lines[0]
        grid = np.array(lines[2:])
    
        to_num = lambda x : True if x == "#" else False
        bool_grid = np.array([list(map(to_num, g)) for g in grid])

        points = []

        draw_img(bool_grid)
        for i in range(bool_grid.shape[0]):
            row = bool_grid[i]
            for j in range(bool_grid.shape[1]):
                if row[j]:
                    points.append(Point(j, i))
        
        grid = Grid(points)

        return key, grid
