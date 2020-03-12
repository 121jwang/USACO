class Board:
	regions = []
	def __init__(self, grid):
		self.grid = grid
	def useGrav(self):
		for c in range(0, 10):
			zeroes = 0
			r = len(self.grid) - 1
			while r >= 0:

				if self.grid[r][c] == 0:
					zeroes = zeroes + 1

				if zeroes > 0 and self.grid[r][c] != 0:
					self.grid[r][c], self.grid[r + zeroes][c] = self.grid[r + zeroes][c], self.grid[r][c]
				r = r - 1

	def findRegions(self):
		## updates regions
		self.regions = []
		
		# Make parellel 2D array for boolean values
		# False means has not been checked
		boolGrid = []
		for x in range(0, len(self.grid)):
			row = []
			for i in range(0, 10):
				row.append(False)
			boolGrid.append(row)

		## Keep going until all grids are checked
		for x in range(0, len(self.grid)):
			for i in range(0, 10):
				queue = []
				currentRegion = []
				if self.grid[x][i] == 0:
					boolGrid[x][i] = True
				if boolGrid[x][i] == False:
					checking = self.grid[x][i]
					queue.append((x, i))
					while len(queue) != 0:
						boolGrid[queue[0][0]][queue[0][1]] = True
						currentRegion.append(queue[0])
						## Check neighbors
						## Checks for: If its within boundaries, if its the same value, if its been checked before
						## Up
						if queue[0][0] != 0 and self.grid[queue[0][0] - 1][queue[0][1]] == checking and boolGrid[queue[0][0] - 1][queue[0][1]] == False:
							queue.append((queue[0][0] - 1, queue[0][1]))
							boolGrid[queue[0][0] - 1][queue[0][1]] = True
						## Down
						if queue[0][0] != len(self.grid) - 1 and self.grid[queue[0][0] + 1][queue[0][1]] == checking and boolGrid[queue[0][0] + 1][queue[0][1]] == False:
							queue.append((queue[0][0] + 1, queue[0][1]))
							boolGrid[queue[0][0] + 1][queue[0][1]] = False
						## Left
						if queue[0][1] != 0 and self.grid[queue[0][0]][queue[0][1] - 1] == checking and boolGrid[queue[0][0]][queue[0][1] - 1] == False:
							queue.append((queue[0][0], queue[0][1] - 1))
							boolGrid[queue[0][0]][queue[0][1] - 1] = True
						## Right
						if queue[0][1] != 9 and self.grid[queue[0][0]][queue[0][1] + 1] == checking and boolGrid[queue[0][0]][queue[0][1] + 1] == False:
							queue.append((queue[0][0], queue[0][1] + 1))
							boolGrid[queue[0][0]][queue[0][1] + 1] = True

						queue.pop(0)

				if len(currentRegion) != 0:
					self.regions.append(currentRegion)
					
			
		

		pass
	def getRegions(self, minRegions):
		## Accessor function but only returns regions that fit min requirements
		returning = []
		for e in self.regions:
			if len(e) >= minRegions:
				returning.append(e)
		return returning

	def destroyRegions(self, toDestroy):
		for e in toDestroy:
			for (x, y) in e:
				self.grid[x][y] = 0
				
	def __str__(self):
		message = ""
		for row in range(0, len(self.grid)):
			for col in range(0, 10):
                		message = message + str(self.grid[row][col])
            		if col == 9:
                		message = message + "\n"
		return message


in_file = open("mooyomooyo.in", "r")
output = open("mooyomooyo.out", "w")



info = map(int, in_file.readline().split())
K = info[1]
height = info[0]

gridArray = []
for i in range(0, height):
	intRow = []
	currentRow = in_file.readline().rstrip()
	for x in range(0, len(currentRow)):
		intRow.append(int(currentRow[x]))
	gridArray.append(intRow)

grid = Board(gridArray)
print "Original"
print grid


grid.findRegions()
regions = grid.getRegions(K)

while len(regions) != 0:
	grid.destroyRegions(regions)
	grid.useGrav()
	grid.findRegions()
	regions = grid.getRegions(K)

print "Done"
print grid

output.write(str(grid))
output.close()



