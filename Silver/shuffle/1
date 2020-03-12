in_file = open("shuffle.in", "r")
output = open("shuffle.out", "w")

cowNum = int(in_file.readline())

goTo = [0] * cowNum
original = [0] * cowNum

cows = map(int, in_file.readline().split())
for x in range(cowNum):
    goTo[x] = cows[x] - 1
    original[goTo[x]] = original[goTo[x]] + 1

always = cowNum

queue = []
for x in range(cowNum):
    if original[x] == 0:
        queue.append(x)
        always = always - 1

while len(queue) != 0:
    print queue
    current = queue[0]

    if original[goTo[current]] - 1 == 0:
        original[goTo[current]] = original[goTo[current]] - 1
        queue.append(goTo[current])
        always = always - 1
    queue.pop(0)

print always
output.write(str(always) + "\n")
