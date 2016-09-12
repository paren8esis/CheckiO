# -*- coding: utf-8 -*-

from itertools import product
import operator
from numpy import arange
from math import sqrt

def is_neighbor(x0, y0, x1, y1, walls):
    delta = max(abs(x1 - x0), abs(y1 - y0))
    for i in arange(0.5, delta, 0.5):
        x = x0 + (x1 - x0) * i / delta
        y = y0 + (y1 - y0) * i / delta
        xs = [int(x), int(x) + 1] if x % 1.0 == 0.5 else [int(round(x))]
        ys = [int(y), int(y) + 1] if y % 1.0 == 0.5 else [int(round(y))]
        new_neighbors = set(product(xs, ys))
        if (not new_neighbors.isdisjoint(walls)):
            return False
    return True

def distance(bat1, bat2):
    [x0, y0], [x1, y1] = bat1, bat2
    return sqrt((x1-x0)**2 + (y1-y0)**2)

def dijkstra(bats, neighbors, alpha):
    # Initialization
    prev = {}
    for bat in bats.keys():
        prev[bat] = -1
    prev[(0,0)] = (0,0)
    bats[(0,0)] = 0

    unvisited = list(bats.keys())
    # Find the shortest path
    while len(unvisited) > 0:
        sorted_bats = sorted(bats.items(), key=operator.itemgetter(1))
        current = sorted_bats[0]
        i = 0
        while (current[0] not in unvisited):
            current = sorted_bats[i]
            i += 1
        unvisited.remove(current[0])
        for neigh in neighbors[(current[0][0], current[0][1])]:
            if (neigh[0] in unvisited):
                alt = current[1] + neigh[1]
                if (alt < bats[neigh[0]]):
                    bats[neigh[0]] = alt
                    prev[neigh[0]] = current[0]
    
    return bats, prev

def checkio(bunker):
    # Find the positions of bats and walls
    walls = set()
    bats = {}
    for i, row in enumerate(bunker):
        for j, cell in enumerate(row):
            if (cell == "B"):
                bats[(i, j)] = float("inf")
            if (cell == "A"):
                alpha = (i, j)
                bats[(i, j)] = float("inf")
            if (cell == "W"):
                walls |= {(i, j)}

    if (alpha == (0,0)):
        return 0

    # Find out neighboring bats
    neighbors = {}
    for bat1 in bats.keys():
        for bat2 in bats.keys():
            if (bat1 == bat2):
                continue
            if (is_neighbor(bat1[0], bat1[1], bat2[0], bat2[1], walls)):
                try:
                    neighbors[bat1].append([bat2, distance(bat1, bat2)])
                except KeyError:
                    neighbors[bat1] = [[bat2, distance(bat1, bat2)]]

    # Run Dijkstra's algorithm for the shortest path
    dist, prev = dijkstra(bats, neighbors, alpha)
    return round(dist[alpha], 2)