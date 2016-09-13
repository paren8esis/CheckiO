# -*- coding: utf-8 -*-

import operator

class Islands:
    def __init__(self, islands):
        # (x,y): [(xParent, yParent), rank, size]
        self.islands = {island: [island, 0, 1] for island in islands}
        self.roots = set(island for island in islands)

    def union(self, is1, is2):
        xRoot = self.find(is1)
        yRoot = self.find(is2)

        if (xRoot == yRoot):
            return

        xV = self.islands[xRoot]
        yV = self.islands[yRoot]
        if (xV[1] < yV[1]):
            xV[0] = yRoot
            yV[2] += xV[2]
            self.roots.discard(xRoot)
        elif (xV[1] > yV[1]):
            yV[0] = xRoot
            xV[2] += yV[2]
            self.roots.discard(yRoot)
        else:
            yV[0] = xRoot
            xV[1] += 1
            xV[2] += yV[2]
            self.roots.discard(yRoot)

    def find(self, island):
        if (self.islands[island][0] != island):
            self.islands[island][0] = self.find(self.islands[island][0])
        return self.islands[island][0]

def checkio(land_map):
    # Find out the coordinates of the islands
    islands = []
    for i, row in enumerate(land_map):
        for j, cell in enumerate(row):
            if (cell == 1):
               islands.append((i,j))

    islands_struct = Islands(islands)
    neighbors = [(0,-1), (0,1), (-1,0), (1,0), (-1,-1), (-1,1), (1,-1), (1,1)]
    for island in islands:
        for neighbor in neighbors:
            island2 = tuple(map(operator.add, island, neighbor))
            if (island2 in islands):
                islands_struct.union(island, island2)
    
    return sorted([islands_struct.islands[root][2] for root in islands_struct.roots])