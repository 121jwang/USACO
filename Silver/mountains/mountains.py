def toBase(coords):
    x = coords[0]
    y = coords[1]

    return (x - y, x + y)

in_file = open("mountains.in", "r")
output = open("mountains.out", "w")

mountNum = int(in_file.readline())
mountains = []
for x in range(0, mountNum):
    mountains.append(map(int, in_file.readline().split()))

bases = []
for mount in mountains:
    bases.append(toBase(mount))
bases = sorted(bases, key=lambda e: (e[0], e[1]))
#print bases

end = -10000000000
visible = 0
for base in bases:
    if end < base[1]:
        visible = visible + 1
        end = base[1]

print visible
output.write(str(visible) + "\n")

