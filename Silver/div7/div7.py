in_file = open("div7.in", "r")
output = open("div7.out", "w")

cowNum = int(in_file.readline())
cows = []

first = [1000000000] * 7
first[0] = 0
last = [0] * 7

total = 0
for i in range(cowNum):
    cows.append(int(in_file.readline()))
    total = (total + cows[-1]) % 7

    first[total] = min(first[total], i + 1)
    last[total] = i + 1

gap = 0
for i in range(0, 7):
    if first[i] <= cowNum:
        gap = max(gap, last[i] - first[i])


#print cows
#print total

size = cowNum

"""
count = 0
totals = [total]

while True:
    newTotals = []

    for i in range(0, len(totals)):
        #print i + size - 1
        #print cowNum
        newTotals.append(totals[i] - cows[i + size - 1])
        if newTotals[-1] % 7 == 0:
            total = newTotals[-1]
            break
    #print "SDFSDFSDFS" + str(totals)
    #print type(cows)
    newTotals.append(totals[-1] - cows[len(totals) - 1])
    totals = newTotals
    #print totals
    #print "YUH" + str(type(totals))
    
    for i in range(1, cowNum - size):
        #print "Removing: " + str(cows[i - 1])
        #print "Adding: " + str(cows[i + size - 1])
        total = total - cows[i - 1] + cows[i + size - 1]
        #print "Total: " + str(total)
        if total % 7 == 0:
            break
    
    if total % 7 == 0:
        break

    size = size - 1
"""  

size = size - 1

size = gap
print size
output.write(str(size) + "\n")
output.close()

