in_file = open("measurement.in", "r")
output = open("measurement.out", "w")

info = map(int, in_file.readline().split())
measurements = info[0]
initial = info[1]

cows = {}
milkMax = initial

changes = []
for x in range(measurements):
    changes.append(map(int, in_file.readline().split()))
changes = sorted(changes)

updates = 0
for change in changes:
    cow = change[1]
    milkChange = change[2]

    if cow in cows:
        cows[cow] = cows[cow] + milkChange
    else:
        cows[cow] = initial + milkChange

    if cows[cow] >= milkMax:
        milkMax = cows[cow]
        updates = updates + 1

    print cows
    print milkMax

print updates
