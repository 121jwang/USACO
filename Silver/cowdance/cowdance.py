import bisect

def canMeet(size, cows, time):
    queue = cows[0:size]
    addIdx = size

    currTime = 0
    queue = sorted(queue)

    point = 0
    while point < len(cows):
        timeSkip = queue[point]
        removed = 0

        ## Decrement by time
        #print (queue)
        #print (timeSkip)
        for i in range(point, len(queue)):
            #print (i)
            queue[i] = queue[i] - timeSkip
            if queue[i] == 0:
                removed = removed + 1

        point = point + removed
        #print (point)
        for i in range(addIdx, min(addIdx + removed, len(cows))):
            bisect.insort(queue, cows[i])

        addIdx = min(addIdx + removed, len(cows))

        currTime = currTime + timeSkip
        if currTime > time:
            return False
    return True

inFile = open("cowdance.in", "r")
output = open("cowdance.out", "w")

cowNum, maxTime = map(int, inFile.readline().split())

cows = []
for i in range(cowNum):
    cows.append(int(inFile.readline()))

mins = 1
maxs = cowNum
while mins != maxs:
    mid = (mins + maxs) / 2
    if (canMeet(mid, cows, maxTime)):
        maxs = mid
    else:
        mins = mid + 1
print (mid)
output.write(str(mid) + "\n")
output.close()