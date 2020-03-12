def getArea(p1, p2, p3, p4):
    return (max(p1[0], p2[0], p3[0], p4[0]) - min(p1[0], p2[0], p3[0], p4[0])) * (max(p1[1], p2[1], p3[1], p4[1])  - min(p1[1], p2[1], p3[1], p4[1]))

in_file = open("reduce.in", "r")
output = open("reduce.out", "w")

cowNum = int(in_file.readline())

cows = []
for x in range(cowNum):
    cows.append(tuple(map(int, in_file.readline().split())))

cowsX = sorted(cows, key = lambda x: x[0])
cowsY = sorted(cows, key = lambda x: x[1])

print cowsX
print cowsY
area = getArea(cowsX[0], cowsX[-1], cowsY[0], cowsY[-1])

print area

# Number of removed for each boundary

for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 4):
            ## [TL, TR, BR, BL]
            rm = [0, 0, 0, 0]
            rm[i] = rm[i] + 1
            rm[j] = rm[j] + 1
            rm[k] = rm[k] + 1

            if cowsX[rm[0]] == cowsY[rm[2]]:
                rm[2] = rm[2] + 1
            if cowsX[-1 - rm[1]] == cowsY[-1 - rm[3]]:
                rm[3] = rm[3] + 1
            
            area = min(area, getArea(cowsX[rm[0]], cowsX[-1 - rm[1]], cowsY[rm[2]], cowsY[-1 - rm[3]]))

            print area

print area

