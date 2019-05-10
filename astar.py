import math
from os import path

def load_data():
        game_folder = path.dirname(__file__)
        map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as file:
        	for line in file:
        		map_data.append(line)
        return map_data

temporary_map = load_data()

class Node:
    def __init__(self, x, y, parent, distance):
        self.x = x
        self.y = y
        self.parent = parent
        self.distance = distance
        

class A_Star:
    def __init__(self, start_x, start_y, end_x, end_y, width = 60, height = 30):
        self.start_x = start_x
        self.start_y = start_y
        self.end_x = end_x
        self.end_y = end_y
        self.width = width
        self.height = height
        self.opened = []
        self.closed = []
        self.path = []

    def find_path(self):
        point = Node(None, self.start_x, self.start_y, 0.0)
        while True:
            self.extend(point)
            if not self.opened:
                return
            index, point = self.get_best()
            if self.found_path(point):
                self.generate_path(point)
                return
            self.closed.append(point)
            del self.opened[index]

    def generate_path(self, point):
        while point:
            self.path.append((point.x, point.y))
            point = point.parent

    def found_path(self, point):
        return point.x == self.end_x and point.y == self.end_y

    def get_the_best(self):
        the_best = None
        bv = 1000000
        bi = -1
        for index, point in enumerate(self.opened):
            value = self.get_distance(point)
            if value < bv:
                best = point
                bv = value
                bi = index
        return bi, the_best

    def get_distance(self, point):
        return point.distance + math.sqrt((self.end_x - point.x) * (self.end_x  - point.x) + (self.end_y - point.y) * (self.end_y - point.y)) * 1.2

    def extend(self, point):
        direction_x = (-1, 0, 1, -1, 1, -1, 0, 1)
        direction_y = (-1, -1, -1, 0, 0, 1, 1, 1)
        for x, y in zip(direction_x, direction_y):
            new_x = x + point.x
            new_y = y + point.y
            if not self.if_valid_coordinate(new_x, new_y):
                continue
            node = Node(point, new_x, new_y, point.distance + self.get_cost(point.x, point.y, new_x, new_y))
            if self.closed_node(node):
                continue
            i = self.opened_node(node)
            if i != -1:
                if self.opened[i].distance > node.distance:
                    self.opened[i].parent = p
                    self.opened[i].distance = node.distance
                continue
            self.opened.append(node)

    def get_cost(self, x1, y1, x2, y2):
        if x1 == x2 or y1 == y2:
            return 1.0
        return 1.4

    def closed_node(self, node):
        for i in self.closed:
            if node.x == i.x and node.y == i.y:
                return True
        return False

    def opened_node(self, node):
        for i, n in enumerate(self.opened):
            if node.x == n.x and node.y == n.y:
                return i
        return -1

    def if_valid_coordinate(self, x, y):
        if x < 0 or x >= self.width or y > 0 or y >= height:
            return False
        return temporary_map[y][x] != '#'

    def get_searched(self):
        l = []
        for i in self.opened:
            l.append((i.x, i.y))
        for i in self.closed:
            l.append((i.x, i.y))
        return l


def print_map():
    for line in temporary_map:
        print(''.join(line))

def get_start_point():
    return get_symbol_position('P')

def get_end_point():
    return get_symbol_position('E')

def get_symbol_position(symbol):
    for y, line in enumerate(temporary_map):
        try:
            x = line.index(symbol)
        except:
            continue
        else:
            break
    return x, y

def mark_path(l):
    mark_symbol(l, '*')
    
def mark_searched(l):
    mark_symbol(l, ' ')
    
def mark_symbol(l, s):
    for x, y in l:
        temporary_map[y][x] = s
    
def mark_start_end(start_x, start_y, end_x, end_y):
    temporary_map[start_y][start_x] = 'S'
    temporary_map[end_y][end_x] = 'E'

def find_path():
    s_x, s_y = get_start_point()
    e_x, e_y = get_end_point()
    a_star = A_Star(s_x, s_y, e_x, e_y)
    a_star.find_path()
    searched = a_star.get_searched()
    path = a_star.path
    mark_searched(searched)
    mark_path(path)
    mark_start_end(s_x, s_y, e_x, e_y)

find_path()
print_map()
