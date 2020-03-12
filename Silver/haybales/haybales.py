## Input: Sorted Array of ints, number
## Output: Index of number in array or the index of the next smallest number in list
def indexOf(array, number):
    upper = len(array) - 1
    lower = 0

    if array[0] > number:
        return 0

    while lower != upper:
        middle = (lower + upper + 1) / 2

        if array[middle] <= number:
            lower = middle
        else:
            upper = middle - 1

    return lower + 1

in_file = open("haybales.in", "r")
output = open("haybales.out", "w")

info = map(int, in_file.readline().split())
haybaleNum = info[0]
queries = info[1]

haybales = sorted(map(int, in_file.readline().split()))
#print haybales

for q in range(queries):
    bounds = map(int, in_file.readline().split())
    
    lowerI = indexOf(haybales, bounds[0] - 1)
    upperI = indexOf(haybales, bounds[1])
    
    #print upperI[1] - lowerI[1] + 1
    output.write(str(upperI - lowerI) + "\n")
output.close()
