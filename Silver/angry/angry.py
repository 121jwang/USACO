in_file = open("angry.in", "r")
output = open("angry.out", "w")

info = map(int, in_file.readline().split())

baleNum = info[0]
cowNum = info[1]

bales = []
for i in range(0, baleNum):
    bales.append(int(in_file.readline()))

bales = sorted(bales)

"""
## How many more bales there are than cows
toComp = baleNum - cowNum

## Get the distance between each bales
betweens = []
for i in range(1, baleNum):
    betweens.append(bales[i] - bales[i - 1])


betweens = sorted(betweens)
"""

maxs = 50000000
mins = 0

while mins != maxs:
    #print "yuh"
    usedCows = 0
    last = 0

    mid = (mins + maxs) / 2

    while last < baleNum:
        #print "yuhss"
        usedCows = usedCows + 1
        current = last + 1

        while current < baleNum and bales[current] - bales[last] <= mid * 2:
            #print "asfdsd"
            current = current + 1
        
        last = current
    #print usedCows
    #print cowNum
    if usedCows <= cowNum:
        maxs = mid
    else:
        mins = mid + 1


print mins
output.write(str(mins) + "\n")
output.close()

"""
if toComp != 0:
    print betweens[toComp - 1]
    output.write(str(betweens[toComp - 1]) + "\n")
else:
    print 1
    output.write("1\n")

output.close()
"""
