## Input: 2D array of strings - region
## Output: Boolean of PCL or not
def isPCL(region):
    length = len(region[0])
    width = len(region)
    
    ## Initialized checked list all false
    checked = [[False for x in range(length)] for y in range(width)]
    colors = []
    queue = []
    regions = -1

    for y in range(width):
        for x in range(length):
            if not checked[y][x]:
                queue.append((x, y))

                while len(queue) != 0:
                    if not checked[queue[0][1]][queue[0][0]]:
                        checked[queue[0][1]][queue[0][0]] = True

                        piece = region[queue[0][1]][queue[0][0]]
                        if piece not in colors:
                            colors.append(piece)
                            if len(colors) > 2:
                                return False
            
                        neighbors = getNeighbors(region, (queue[0][0], queue[0][1]))
                        for neighbor in neighbors:
                            queue.append(neighbor)
                        print "Queue"
                        print queue
                        if not checkColors(region, checked, queue[0]):
                            regions = regions + 1
                        print "Regions"
                        print regions
                        if regions > 3:
                            return False
                    queue.pop(0)
    if regions == 3:
        return True
    return False
## loc is tuple (x,y)
def getNeighbors(region, loc):
    x = loc[0]
    y = loc[1]
    neighbors = []

    if y - 1 >= 0:
        neighbors.append((x, y - 1))
    if y + 1 < len(region):
        neighbors.append((x, y + 1))
    if x - 1 >= 0:
        neighbors.append((x - 1, y))
    if x + 1 < len(region[0]):
        neighbors.append((x + 1, y))
    return neighbors

def checkColors(region, checked, loc):
    neighbors = getNeighbors(region, loc)

    ogClr = region[loc[1]][loc[0]]

    for neighbor in neighbors:
        print "Neighbors"
        print neighbor
        print checked
        print region
        if not checked[neighbor[1]][neighbor[0]] and region[neighbor[1]][neighbor[0]] == region[loc[1]][loc[0]]:
            return True
    return False



print isPCL([["A", "B", "B"],["B", "B", "B"],["A", "A", "B"],["A","B","B"]])
print isPCL([["B","C"],["B","C"],["B","B"],["B","C"]])

print isPCL([["A","B","B","A"]])
