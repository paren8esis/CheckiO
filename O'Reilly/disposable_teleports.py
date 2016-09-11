# -*- coding: utf-8 -*-

def checkio(teleports_string):
    neighs = {}
    teleports_string = teleports_string.split(",")
    for teleport in teleports_string:
        if (teleport[0] not in neighs.keys()):
            neighs[teleport[0]] = set([teleport[1]])
        else:
            neighs[teleport[0]].add(teleport[1])
        if (teleport[1] not in neighs.keys()):
            neighs[teleport[1]] = set([teleport[0]])
        else:
            neighs[teleport[1]].add(teleport[0])
    
    # Run BFS algorithm
    queue = [("1", ["1"], set(teleports_string))]

    while queue:
        current, path, teleports = queue.pop(0)
        if (current == "1") and (len(set(path)) == 8):
            return "".join(path)
        for neigh in neighs[current]:
            if (neigh + current in teleports) or (current + neigh in teleports):
                queue.append((neigh, path + [neigh], teleports - {neigh + current} - {current + neigh}))