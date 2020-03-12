in_file = open("cbarn.in", "r")
output = open("cbarn.out", "w")

cowNum = int(in_file.readline())

ring = []
for x in range(cowNum):
    loc = int(in_file.readline())
    ring.append(loc)

start = ring.index(max(ring))

activeCows = ring[start]
cost = 0

cowList = [[start, activeCows]]

#print "Starting at index: " + str(start)

counter = []
for i in range(cowNum):
    counter.append(i)

for i in range(1, cowNum + 1):
    currIndex = (start + i) % cowNum

    if ring[currIndex] != 0:
        cowList.append([currIndex, ring[currIndex]])

    #print currIndex
    #print cowList
    
    if len(cowList) == 0:
        continue
    cost = cost + (counter[currIndex - cowList[0][0]])**2

    if cowList[0][1] > 0:
        cowList[0][1] = cowList[0][1] - 1
    if cowList[0][1] == 0:
        cowList.pop(0)
    
    #print "New Cost: " + str(cost)

print cost

output.write(str(cost) + "\n")
output.close()
