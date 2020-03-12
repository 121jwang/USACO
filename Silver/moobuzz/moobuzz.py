## Returns the number of moos
def getMoos(num):
    return int(num / 5) + int(num / 3) - int(num / 15)

inFile = open("moobuzz.in", "r")
output = open("moobuzz.out", "w")

target = int(inFile.readline())

mins = 0
maxs = 10000000000

while True:
    mid = int((mins + maxs) / 2)
    moos = getMoos(mid)

    if mid - moos == target:
        break
    elif mid - moos > target:
        maxs = mid
    else:
        mins = mid

print (mid)
output.write(str(mid) + "\n")
output.close()