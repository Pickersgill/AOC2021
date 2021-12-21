import numpy as np
from PIL import Image

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "<%d, %d>" % (self.x, self.y)

class Grid:
    def __init__(self, init_points=None):
        self.point_map = self.load_map(init_points)
        
    def load_map(self, ps):
        new_map = {}

        for p in ps:
            new_map[(p.x, p.y)] = p
    
        return new_map

    def get_bounds(self):
        min_x, min_y, max_x, max_y = None, None, None, None
        for p in self.point_map.values():
            cx = p.x
            cy = p.y

            max_x = cx if max_x is None or cx > max_x else max_x
            max_y = cy if max_y is None or cy > max_y else max_y
            min_x = cx if min_x is None or cx < min_x else min_x
            min_y = cy if min_y is None or cy < min_y else min_y
    
    
        return [min_x-1, min_y-1, max_x+1, max_y+1]

    def does_exist(self, x, y):
        try:
            if self.point_map[(x, y)]:
                return True
        except KeyError:
            return False

    def compute_val(self, x, y):
        OFFSETS = [
                    [-1, -1], [0, -1], [1, -1], 
                    [-1,  0], [0,  0], [1,  0],
                    [-1,  1], [0,  1], [1 , 1]
                  ]

        bin_str = ""
    
        for of in OFFSETS:
            is_on = self.does_exist(x + of[0], y + of[1])
            bin_str += "1" if is_on else "0"
            
        print(bin_str, int(bin_str, 2))
        return int(bin_str, 2)
    
    def number_of_on(self):
        return len(self.point_map.keys())
    
    def get_transformation(self, key):
        bounds = self.get_bounds()
        new_points = []
        print(bounds)
        for x in range(bounds[0], bounds[2]+1):
            for y in range(bounds[1], bounds[3]+1):
                new_val = key[self.compute_val(x, y)]
                if new_val == "#":
                    new_points.append(Point(x, y))

        new_grid = Grid(new_points)
        return new_grid

