in_file = open("hopscotch.in", "r")
output = open("hopscotch.out", "w")

R, C, K = map(int, in_file.readline().split())

grid = []
for x in range(R):
    grid.append(map(int, in_file.readline().split()))

#print grid

visits = [[0 for j in range(R)] for i in range(C)]
visits[0][0] = 1

for i in range(0, R):
    for j in range(0, C):
        for k in range(i + 1, R):
            for z in range(j + 1, C):
                ## different numbers
                if grid[i][j] != grid[k][z]:
                    visits[k][z] = (visits[k][z] + visits[i][j]) % 1000000007

#print visits[R- 1][C - 1]

output.write(str(visits[R - 1][C - 1]) + "\n")
output.close()