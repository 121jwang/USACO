in_file = open("maxcross.in", "r")
output = open("maxcross.out", "w")

info = map(int, in_file.readline().rstrip().split())
walkNum = info[0]
minSize = info[1]
broken  = info[2]

crosswalks = [True] * walkNum
for light in range(0, broken):
    index = int(in_file.readline().rstrip()) - 1
    crosswalks[index] = False

#print crosswalks

minLights = 0
fixed = 0
broken = 0
for light in range(0, minSize):
    if crosswalks[light]:
        fixed = fixed + 1
    else:
        broken = broken + 1
minLights = broken
for startPos in range(1, walkNum - minSize):
    if crosswalks[startPos - 1]:
        fixed = fixed - 1
    else:
        broken = broken - 1
    if crosswalks[startPos + minSize - 1]:
        fixed = fixed + 1
    else:
        broken = broken + 1

    minLights = min(minLights, broken)

output.write(str(minLights) + "\n")
output.close()
