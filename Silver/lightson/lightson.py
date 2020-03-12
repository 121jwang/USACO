in_file = open("lightson.in", "r")
output = open("lightson.out", "w")


info = map(int, in_file.readline().split())
size = info[0]
switchNum = info[1]

grid = [[0 for x in range(size)] for y in range(size)]

switchInfo = {}
for x in range(switchNum):
    info = map(int, in_file.readline().split())

    origin = (info[0] - 1, info[1] - 1)
    final = (info[2] - 1, info[3] - 1)
    
    try:
        switchInfo[origin].append(final)
    except:
        switchInfo[origin] = [final]

    grid[final[0]][final[1]] = grid[final[0]][final[1]] + 1



count = 1
while count != 0:
    ## Find region that bessie can visit
    queue = [(0, 0)]
    region = [(0, 0)]
    while len(queue) != 0:
        curr = queue[0]
        x = curr[0]
        y = curr[1]
    
        neighbors = []
        if x - 1 >= 0:
            neighbors.append((x-1, y))
        if x + 1 < size:
            neighbors.append((x+1, y))
        if y - 1 >= 0:
            neighbors.append((x, y-1))
        if y + 1 < size:
            neighbors.append((x, y+1))
    
        #print neighbors
        for n in neighbors:
            #print n
            if grid[n[0]][n[1]] != 0 and n not in region:
                region.append(n)
                queue.append(n)
        queue.pop(0)

    #print region
    
    count = 0
    ## Remove everything outside of the region
    for x in range(size):
        for y in range(size):
            if (x, y) in switchInfo and (x, y) not in region:
                for switch in switchInfo[(x, y)]:
                    grid[switch[0]][switch[1]] = grid[switch[0]][switch[1]] - 1
                    count = count + 1
                del switchInfo[(x, y)]

#print len(region)

output.write(str(len(region)) + "\n")
output.close()
