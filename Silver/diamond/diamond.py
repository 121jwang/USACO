def solve(dList, maxSpread):
    diamondsIn = []
    count = 0
    for x in range(maxSpread + 1):
        count = count + dList[x]
    diamondsIn.append([count, 0])
    
    for x in range(1, len(dList) - maxSpread):
        count = count + dList[x + maxSpread]
        count = count - dList[x - 1]
        diamondsIn.append([count, x])

    return diamondsIn

in_file = open("diamond.in", "r")
output = open("diamond.out", "w")

info = map(int, in_file.readline().split())
diamondNum = info[0]
maxSpread = info[1]

locs = []
for x in range(diamondNum):
    locs.append(int(in_file.readline()) - 1)

dList = [0] * (max(locs) + 1)

for loc in locs:
    dList[loc] = dList[loc] + 1

diamondsIn = solve(dList, maxSpread)

caseOne = max(diamondsIn)

for x in range(caseOne[1], caseOne[1] + maxSpread + 1):
    dList[x] = 0

diamondsIn = solve(dList, maxSpread)

caseTwo = max(diamondsIn)

output.write(str(caseOne[0] + caseTwo[0]) + "\n")
output.close()
