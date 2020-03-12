def getHPSNum(hpsList):
    hoof = 0
    paper = 0
    scissor = 0
    for x in hpsList:
        if x == "H":
            hoof = hoof + 1
        elif x == "P":
            paper = paper + 1
        else:
            scissor = scissor + 1
    return [hoof, paper, scissor]

in_file = open("hps.in", "r")
output = open("hps.out", "w")

hpsList = []

for x in range(0, int(in_file.readline().rstrip())):
    hpsList.append(in_file.readline().rstrip())

print hpsList

hpsInfo = getHPSNum(hpsList)

firstSection = [0, 0, 0]
secondSection = list(hpsInfo)
currentWins = 0
maxWins = 0
change = 0
for x in range(0, len(hpsList)):
    if hpsList[x] == "H":
        change = 0
    elif hpsList[x] == "P":
        change = 1
    else:
        change = 2

    firstSection[change] = firstSection[change] + 1
    secondSection[change] = secondSection[change] - 1

    currentWins = max(firstSection) + max(secondSection)

    if currentWins > maxWins:
        maxWins = currentWins

print maxWins
output.write(str(maxWins) + "\n")
output.close()
