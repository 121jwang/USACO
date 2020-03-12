in_file = open("buckets.in", "r")
output = open("buckets.out", "w")

grid = []

rockI = (0, 0)
barnI = (0, 0)
lakeI = (0, 0)

for x in range(0, 10):
    line = in_file.readline()
    toAdd = []
    for y in range(0, 10):
        char = line[y]
        if char == "L":
            toAdd.append(3)
            lakeI = (x, y)
        elif char == "B":
            toAdd.append(2)
            barnI = (x, y)
        elif char == "R":
            toAdd.append(1)
            rockI = (x, y)
        else:
            toAdd.append(0)

    grid.append(toAdd)


answer = 0
print barnI
print lakeI
if barnI[0] - lakeI[0] != 0:
    answer = abs(barnI[0] - lakeI[0]) + abs(barnI[1] - lakeI[1]) - 1
else:
    if rockI[1] in range(min(barnI[1], lakeI[1]), max(barnI[1], lakeI[1]) + 1):
        answer = abs(barnI[1] - lakeI[1]) + 1
    else:
        answer = abs(barnI[1] - lakeI[1]) - 1

print answer
output.write(str(answer) + "\n")
output.close()
