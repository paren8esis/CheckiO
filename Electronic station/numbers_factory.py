import math

# Fill in the dictionary in such a way that:
# Starting from the root (data), we find its divisors and remainders [div, rem].
# For every remainder, do the same process.
# So we end up with a tree of the form:
#           20
#       /   |   \
#   [2,10] [4,5] [5,4]
#   /   |     |     |      
#[2,5] [5,2] [5,1] [4,1]
#  |     |
#[5,1] [2,1]
#
def fillInDict(data, numDict):
    if (data < 10):
        numDict[data] = []
        numDict[data].append([data, 1])
        return
    numDict[data] = []
    for i in range(2, 10):
        ypol = data/i
        if (math.floor(ypol) == ypol):
            numDict[data].append([i, ypol])
            fillInDict(ypol, numDict)
            
    if (numDict[data] == []):
        numDict[data].append([data, 0])

def BFS(root, numDict):
    queue = [[[root,root]]]

    paths = []  # Holds the valid paths for the same level
    while (len(queue) != 0):
        path = queue.pop(0)
        if (len(paths) != 0) and (len(path) > len(paths[0])):
            break
        father = path[-1]
        if (father[1] == 1):
            paths.append(path)
            continue
        if (father[1] == 0):
            continue
        else:
            divisors = numDict[father[1]]
            for divisor in divisors:
                newPath = list(path)
                newPath.append(divisor)
                queue.append(newPath)
    
    # Calculate numbers whose product of digits == data
    # and return the smallest one
    num = float("inf")
    for path in paths:
        num2 = 0
        for i in range(1, len(path)):
            num2 = (num2*10) + path[i][0]
        if (num2 < num):
            num = num2
    
    if (num == float("inf")):
        return 0
    else:
        return num
        
# numDict = {
#  number: [[divisor1, remainder1], [divisor2, remainder2], ...]
# }
def checkio(data):
    numDict = {}
    numDict[data] = []
    fillInDict(data, numDict)
    
    return BFS(data, numDict)
