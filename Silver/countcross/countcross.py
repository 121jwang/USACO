from collections import Counter
import math

class Field:
    def __init__(self):
        self.cow = False
        self.visited = False
        self.connections = []
    def setVisited(self, visit):
        self.visited = True
    def setNeighbors(self, roads):
        self.connections = roads
    def setCow(self, cow):
        self.cow = cow
    def __str__(self):
        return str(self.visited)

in_file = open("countcross.in", "r")
output = open("countcross.out", "w")

info = map(int, in_file.readline().rstrip().split())
fieldCount = info[0]
cowCount   = info[1]
roadCount  = info[2]

roads = {}
for i in range(0, roadCount):
    road = map(int, in_file.readline().rstrip().split())
    try:
        roads[road[0] - 1, road[1] - 1].append((road[2] - 1, road[3] - 1))
    except:
        roads[road[0] - 1, road[1] - 1] = []
        roads[road[0] - 1, road[1] - 1].append((road[2] - 1, road[3] - 1))
    try:
        roads[road[2] - 1, road[3] - 1].append((road[0] - 1, road[1] - 1))
    except:
        roads[road[2] - 1, road[3] - 1] = []
        roads[road[2] - 1, road[3] - 1].append((road[0] - 1, road[1] - 1))
#print roads
cows = []
for i in range(0, cowCount):
    cow = map(int, in_file.readline().rstrip().split())
    cows.append((cow[0] - 1, cow[1] - 1))

fields = [[Field() for x in range(fieldCount)] for i in range(fieldCount)]

for key in roads:
    neighbors = roads[key]
    fields[key[1]][key[0]].setNeighbors(neighbors)
    #print fields[key[0]][key[1]].connections

for cow in cows:
    fields[cow[1]][cow[0]].setCow(True)

region = 0
cowInRegion = 0
cowPerRegion = []
for x in range(fieldCount):
    for y in range(fieldCount):
        queue = []
        #print fields
        if not fields[y][x].visited:
            #print "entered"
            cowInRegion = 0
            queue.append((x, y))
            while len(queue) != 0:
                #print "queue: " + str(queue)
                x1 = queue[0][0]
                y1 = queue[0][1]
                if not fields[y1][x1].visited:
                    fields[y1][x1].setVisited(True)
                    if fields[y1][x1].cow:
                        cowInRegion = cowInRegion + 1
                    neighbors = []
                    if y1 - 1 >= 0:
                        neighbors.append((x1, y1 - 1))
                    if y1 + 1 < fieldCount:
                        neighbors.append((x1, y1 + 1))
                    if x1 - 1 >= 0:
                        neighbors.append((x1 - 1, y1))
                    if x1 + 1 < fieldCount:
                        neighbors.append((x1 + 1, y1))
                    #print "Potentials: " + str(neighbors)
                    #print "Neighbors: " + str(fields[y1][x1].connections)
                    for n in neighbors:
                        if n not in fields[y1][x1].connections and not fields[n[1]][n[0]].visited:
                            #print "Adding: " + str(n)
                            queue.append(n)
                queue.pop(0)
            #print "END"
            cowPerRegion.append(cowInRegion)
#print cowPerRegion

totalCows = cowCount
multiplier = 1
answer = 0
#print cowPerRegion
for num in cowPerRegion:
    answer = answer + num * (totalCows - num)
    totalCows = totalCows - num

print answer

#answer = math.factorial(len(cowPerRegion))/2 * multiplier
output.write(str(answer) + "\n")
