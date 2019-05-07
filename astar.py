import math
from os import path

def load_data():
    game_folder = path.dirname(__file__)
    map_data = []
    with open(path.join(game_folder, 'map.txt'), 'rt') as f:
        for line in f:
            map_data.append(line)


class Node_Element:
    def __init__(self, parent, x, y, distance):
        self.parent = parent
        self.x = x
        self.y = y
        self.distance = distance


class A_Star:
    def __init__(self, start_x, start_y, end_x, end_y, width = 60, height = 30):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.eng_y = end_y
        self.width = width
        self.height = height
        self.open_set[]
        self.closed_set[]
        self.path[]

    def find_path(self):
        point = Node_Element(None, self.start_x, self.start_y, 0.0)
        while True:
            self.extend_round(point)
