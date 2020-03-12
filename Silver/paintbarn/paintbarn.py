in_file = open("paintbarn.in", "r")
output = open("paintbarn.out", "w")

info = map(int, in_file.readline().rstrip().split())
rectangles = info[0]
coats = info[1]
#print coats
grid = [[0 for x in range(1001)] for i in range(1001)]
#print grid

for i in range(0, rectangles):
    rect = map(int, in_file.readline().rstrip().split())
    for x in range(rect[0], rect[2]):
        grid[x][rect[1]] = grid[x][rect[1]] + 1
        grid[x][rect[3]] = grid[x][rect[3]] - 1
    #print grid
area = 0
for x in range(0, 1000):
    for y in range(0, 1000):
        if grid[x][y] == coats:
            area = area + 1
        grid[x][y + 1] = grid[x][y + 1] + grid[x][y]
print area
output.write(str(area) + "\n")
output.close()
#print grid
