import math

def computeManhattanDist(curr, goal):
	# Computes the manhattan distance from given node to goal.
	manhDst = abs(curr[0] - goal[0]) + abs(curr[1] - goal[1])
	return manhDst

def findPossibleMoves(x, y, s, goal, data):
	# Finds all possible moves from current position and
	# adds node to state space accordingly.
	# Note: If node is already in state space, this method checks whether its g cost is
	# higher than the new node's. If it is, it replaces it with the new node.
	
	possibleMoves = []
	if (x - 1 >= 0) and (data[x - 1][y] != 1):
		manDst = computeManhattanDist((x-1, y), goal)
		if ((x-1, y) not in list(s.keys())) or (((x-1, y) in list(s.keys())) and (s[(x-1, y)][2] > s[(x,y)][1] + 1 + manDst)):
			s = addNode(s, (x-1, y), (x, y))
			s[(x-1, y)][2] = 1 + manDst
			possibleMoves.append((x-1, y))
	if (x + 1 <= len(data)-1) and (data[x + 1][y] != 1):
		manDst = computeManhattanDist((x+1, y), goal)
		if ((x+1, y) not in list(s.keys())) or (((x+1, y) in list(s.keys())) and (s[(x+1, y)][2] > s[(x,y)][1] + 1 + manDst)):
			s = addNode(s, (x+1, y), (x, y))
			s[(x+1, y)][2] = 1 + manDst
			possibleMoves.append((x+1, y))
	if (y + 1 <= len(data[0])-1) and (data[x][y + 1] != 1):
		manDst = computeManhattanDist((x, y+1), goal)
		if ((x, y+1) not in list(s.keys())) or (((x, y+1) in list(s.keys())) and (s[(x, y+1)][2] > s[(x,y)][1] + 1 + manDst)):
			s = addNode(s, (x, y+1), (x, y))
			s[(x, y+1)][2] = 1 + manDst
			possibleMoves.append((x, y+1))
	if (y - 1 >= 0) and (data[x][y - 1] != 1):
		manDst = computeManhattanDist((x, y-1), goal)
		if ((x, y-1) not in list(s.keys())) or (((x, y-1) in list(s.keys())) and (s[(x, y-1)][2] > s[(x,y)][1] + 1 + manDst)):
			s = addNode(s, (x, y-1), (x, y))
			s[(x, y-1)][2] = 1 + manDst
			possibleMoves.append((x, y-1))

	return possibleMoves
    
def addToOpenSet(openSet, newNodes, s):
    # Adds the new nodes to openSet in sorted order,
    # according to the estimated cost to goal.

    for newNode in newNodes:
        added = False
        for node in openSet:
            if (s[node][2] > s[newNode][2]):
                openSet.insert(openSet.index(node), newNode)
                added = True
                break
        if (not added):
            openSet.append(newNode)
    
    return openSet
    
def a_star(currPosX, currPosY, goalX, goalY, data, res):
    # A* algorithm.
    # Computes next best move, for only one square in the room.
    
    goal = (goalX, goalY)
    stateSpace = {}
    stateSpace[(currPosX, currPosY)] = [None, 0, 0, True, []]

    # Expand from current position
    possibleMoves = findPossibleMoves(currPosX, currPosY, stateSpace, goal, data)
    
    closedSet = [(currPosX, currPosY)]   # List of nodes already evaluated 
    
    openSet = addToOpenSet([], possibleMoves, stateSpace)   # List of nodes yet to be evaluated
    cameFrom = {}
    
    current = [-1, -1]
    
    while (len(openSet) != 0):
        current = openSet.pop(0)
        if (current == goal):
            break
            
        closedSet.append(current)

        children = findPossibleMoves(current[0], current[1], stateSpace, goal, data)
        for child in children:
            tentative_g_score = stateSpace[current][1] + 1
            try:
                closedSet.index(child)
                if (tentative_g_score >= stateSpace[child][1]):
                    continue
            except ValueError:
                pass
                
            inOpen = False
            try:
                openSet.index(child)
                inOpen = True
            except ValueError:
                pass
                
            if (not inOpen):
                cameFrom[child] = current
                stateSpace[child][1] = tentative_g_score
                stateSpace[child][2] = tentative_g_score + computeManhattanDist(child, goal)
                openSet = addToOpenSet(openSet, [child], stateSpace)
            else:
                if (tentative_g_score < stateSpace[child][1]):
                    cameFrom[child] = current
                    stateSpace[child][1] = tentative_g_score
                    stateSpace[child][2] = tentative_g_score + computeManhattanDist(child, goal)

    while (current in list(cameFrom.keys())):
        current = cameFrom[current]
        
    if (currPosX == current[0]):
        if (currPosY > current[1]):
            res += 'W'
        else:
            res += 'E'
    else:
        if (currPosX > current[0]):
            res += 'N'
        else:
            res += 'S'
    
    return [current, res]

def addNode(s, coord, parent):
	# Adds a node to the state space s.  
    # s is the data structure that holds the tree.
	# It is a dictionary with elements of the form:
	# KEY : Node coordinates 
	# VALUE : [ 0 -> parent,
	#   1 -> cost from start
	#   2 -> estimated cost to goal,
	#   3 -> isLeaf,
	#   4 -> list of children
	# ]
    
    if (coord not in list(s.keys())):
        s[parent][3] = False
        s[parent][4].append(coord)	

		# Compute cost from start
        g = 1
        nextPar = s[parent][0]
        while (nextPar != None):
            g += 1
            nextPar = s[nextPar][0]
            
        s[coord] = [parent, g, 0, True, []]
        
    return s
    
def checkio(data):
    res = ""
    
    x1 = 1
    y1 = 1
    
    while ((x1 != 10) or (y1 != 10)):
        # Until we reach the exit
        pos = a_star(x1, y1, 10, 10, data, res)
        x1 = pos[0][0]
        y1 = pos[0][1]
        res = pos[1]
        
    return res
