# Given a list of tuples of ((x,y), radius) representing cell towers
# and an x,y coordinate representing a cell phone,
# find the closest cell tower within range.


# This implementation uses a hashmap that maps coordinates to lists of towers.
# The granularity of the coordinates is the max radius of the towers * 2.

# This implementation assumes that the coordinates are integers.

from collections import namedtuple
from math import inf

Point = namedtuple('Point', ['x', 'y'])
Tower = namedtuple('Tower', ['coords', 'radius'])

class TowerFinder:
    def __init__(self):
        self.towers = []
        self.max_radius = -inf
        self.processed_towers = {}

    def add_tower(self, tower):
        if tower.radius > self.max_radius:
            self.max_radius = tower.radius
        self.towers.append(tower)
        preprocess_towers()

    def preprocess_towers(self):
        self.processed_towers = {self.alias(tower): tower for tower in self.towers}

    def alias(self, coords):
        radius = self.max_radius * 2
        x = (coords.x // radius) * radius
        y = (coords.y // radius) * radius
        return Point(x, y)

    def find_closest(self, coord):
        min_dist = inf
        closest_tower = None
        for tower in self.processed_towers[self.alias(coord)]:
            dist = self.distance(coord, tower.coords)
            if dist < min_dist:
                min_dist = dist
                closest_tower = tower
        return closest_tower

