in_file = open("perimeter.in", "r")
output = open("perimeter.out", "w")

size = int(in_file.readline().rstrip())
cones = []
visited = []
for x in range(0, size):
    cones.append(list(in_file.readline().rstrip()))
    visited.append([False] * size)
#print cones
maxPerimeter = 0
maxArea = 0
for x in range(size):
    for y in range(size):
        queue = []
        perimeter = 0
        area = 0
        if not visited[y][x] and cones[y][x] == "#":
            queue.append((x, y))
            while len(queue) != 0:
                x1 = queue[0][0]
                y1 = queue[0][1]
                if not visited[y1][x1]:
                    visited[y1][x1] = True
                    area = area + 1
                    neighbors = []
                    if y1 - 1 >= 0:
                        neighbors.append((x1, y1 - 1))
                    if y1 + 1 < size:
                        neighbors.append((x1, y1 + 1))
                    if x1 - 1 >= 0:
                        neighbors.append((x1 - 1, y1))
                    if x1 + 1 < size:
                        neighbors.append((x1 + 1, y1))
                    
                    add = 0
                    for n in neighbors:
                        #print n
                        if cones[n[1]][n[0]] == "#":
                            add = add + 1
                            queue.append(n)
                    #print queue
                    perimeter = perimeter + (4 - add)
                queue.pop(0)
            #print "End Region"
            if area == maxArea:
                maxPerimeter = max(maxPerimeter, perimeter)
            if area > maxArea:
                maxArea = area
                maxPerimeter = perimeter
output.write(str(maxArea) + " " + str(maxPerimeter)  + "\n")
