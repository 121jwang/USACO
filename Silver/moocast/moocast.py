def getBroadcasts(current, hear, transmits):
    #print "HEY" + str(current)
    #print len(hear)
    
    ## Already broadcasted
    if hear[current]:
        return 0
    
    #print current
    #print len(hear)
    

    hear[current] = True
    ret = 1
    for x in transmits[current]:
        ret = ret + getBroadcasts(x[0], hear, transmits)
    
    return ret

in_file = open("moocast.in", "r")
output = open("moocast.out", "w")

cowNum = int(in_file.readline())

cows = []
for x in range(cowNum):
    cows.append(map(int, in_file.readline().split()))

#print cows

transmits = []
for x in range(cowNum):
    toAdd = []
    for y in range(cowNum):
        ## Get Distance Range with distance formula
        distance = ((cows[x][0] - cows[y][0])**2 + (cows[x][1] - cows[y][1])**2)**0.5
        #print distance
        if distance <= cows[x][2]:
            #print "dab"
            ## Add the index and cow info for recursive use
            toAdd.append((y, cows[y]))

    #print "yeet"
    transmits.append(toAdd)

#print transmits
ret = 1
for x in range(cowNum):
    hear = [False] * cowNum
    ret = max(ret, getBroadcasts(x, hear, transmits))

print ret

output.write(str(ret) + "\n")
