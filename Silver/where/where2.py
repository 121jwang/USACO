## Input: Top Left and Bottom Right (x1, y1), (x2, y2)
## Output: Colors of each region ["Color", "Color"...]
def getSubs(corner, corner2):
    # Check for cached results
    """
    try:
        info = regions[(corner, (corner2[0], corner2[1] - 1))]
        colors = set(info)
        
        # Cannot be a PCL
        if len(colors) > 2:
            return ["A", "B", "C"]
         
    except:
        # There is no cached info
        pass
    """
    checked = [[False for x in range(20)] for y in range(20)]
    regions = []

    for x in range(corner[0], corner2[0] + 1):
        for y in range(corner[1], corner2[1] + 1):
            queue = []
            #print x, y
            #print checked
            if not checked[y][x]:
                queue.append((x, y))
                while len(queue) != 0:
                    checked[queue[-1][1]][queue[-1][0]] = True
                    color = grid[queue[-1][1]][queue[-1][0]]
                
                    neighbors = getNeighbors((queue[-1][0], queue[-1][1]), corner, corner2)
                    
                    #print grid
                    #print checked
                    queue.pop(-1)
                    for n in neighbors:
                        #print n
                        if grid[n[1]][n[0]] == color and not checked[n[1]][n[0]]:
                            #print n
                            queue.append(n)
                
                #print "NEW REGION"
                #print x, y
                #print checked
                regions.append(color)
    return regions

def getNeighbors(pos, corner, corner2):
    neighbors = []

    x = pos[0]
    y = pos[1]
    if y - 1 >= corner[1]:
        neighbors.append((x, y - 1))
    if y + 1 <= corner2[1]:
        neighbors.append((x, y + 1))
    if x - 1 >= corner[0]:
        neighbors.append((x - 1, y))
    if x + 1 <= corner2[0]:
        neighbors.append((x + 1, y))
    return neighbors

def isPCL(subRegions):

    if len(set(subRegions)) == 2:
        if (subRegions.count(list(set(subRegions))[0]) == 1) != (subRegions.count(list(set(subRegions))[1]) == 1):
            return True
    return False

def inPCL(a, b):
    return a[0] >= b[0] and a[2] <= b[2] and a[1] >= b[1] and a[3] <= b[3]

in_file = open("where.in", "r")
output = open("where.out", "w")

lines = int(in_file.readline())
grid = []

for x in range(lines):
    grid.append(list(in_file.readline().rstrip()))

## Key1: Start Pos (x, y)
## Key2: Bottom Right (x, y)
## Value = Colors of each regions ["Color", "Color"...]
regions = {}

PCLS = []
for x1 in range(0, lines):
    for y1 in range(0, lines):
        for x2 in range(x1, lines):
            for y2 in range(y1, lines):
                #print i1, j1, i2, j2
                PCLInfo = getSubs((x1, y1), (x2, y2))
                if isPCL(PCLInfo): 
                    PCLS.append([x1, y1, x2, y2])
                    #regions[(x1, y1), (x2, y2)] = PCLInfo

#print regions

#PCLS = sorted(PCLS)
PCLNum = 0
for x in range(0, len(PCLS)):
    PCLAdd = True
    for i in range(0, len(PCLS)):
        if x != i and inPCL(PCLS[x], PCLS[i]):
            PCLAdd = False
            break
    if PCLAdd:
        #print PCLS[x]
        PCLNum = PCLNum + 1

output.write(str(PCLNum) + "\n")
output.close()
"""
print isPCL(getSubs([(0, 0), (3, 4)]))
print isPCL(getSubs([(2, 0), (2, 4)]))
print isPCL(getSubs([(2, 0), (1, 1)]))
"""
