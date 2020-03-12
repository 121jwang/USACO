in_file = open("herding.in", "r")
output = open("herding.out", "w")

consCows = int(in_file.readline().rstrip())
cows = []
for x in range(0, consCows):
    cow = int(in_file.readline().rstrip())
    cows.append(cow)
cows = sorted(cows)

## Solve for minimum
# Check for corner cases
minSwitch = 0
if cows[-2] - cows[0] == consCows - 2 and cows[-1] - cows[-2] > 2:
    minSwitch = 2
elif cows[-1] - cows[1] == consCows - 2 and cows[1] - cows[0] > 2:
    minSwitch = 2
else:
    j = 0
    cowsInRegion = 0
    for i in range(0, consCows):
        while j < consCows - 1 and cows[j + 1] - cows[i] <= consCows - 1:
            j = j + 1
        cowsInRegion = max(cowsInRegion, j - i + 1)
    minSwitch = consCows - cowsInRegion

print minSwitch

maxSwitch = max(cows[-2] - cows[0], cows[-1] - cows[1]) - (consCows - 2)
print maxSwitch

output.write(str(minSwitch) + "\n" + str(maxSwitch) + "\n")
output.close()
