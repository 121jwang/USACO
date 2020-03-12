in_file = open("citystate.in", "r")
output = open("citystate.out", "w")

count = int(in_file.readline())

occurs = {}

specialPairs = 0
for i in range(count):
    info = in_file.readline().split()
    
    city = info[0][0:2]
    state = info[1]

    if city != state:
        combo = city + state
        if combo not in occurs:
            occurs[combo] = 0
        occurs[combo] = occurs[combo] + 1

for key in occurs:
    pair = key[2:] + key[0:2]
    if pair in occurs:
        specialPairs = specialPairs + occurs[pair] * occurs[key]

specialPairs = specialPairs / 2

print specialPairs
output.write(str(specialPairs) + "\n")
output.close()
