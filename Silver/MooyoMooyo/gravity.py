def shift(array):
	currentIndex = 0
	x = 0
	zeroCount = 0

	while x < len(array):
		currentIndex = x
		if array[x] == 0:
			#swapping down
			for i in range(currentIndex + 1, len(array)):
				if array[i] != 0:
					array[i], array[x] = array[x], array[i]
					break
		x = x + 1

array = [7, 0, 9, 0, 0, 3, 2, 0, 0, 0, 4]
shift(array)
print array



