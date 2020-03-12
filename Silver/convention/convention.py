## Returns the wait times of each bus

"""
def getMaxWait(cows, busNum, seatNum):
	cowNum = len(cows)
	if cowNum <= busNum:
		return [0]
	if busNum == 1:
		return [cows[-1] - cows[0]]

	wait   = getMaxWait(cows[:cowNum - seatNum], busNum - 1, seatNum)
	
	## Find seatNum for current bus
	seats = seatNum
	currentGroup = cows[cowNum - seatNum - 1:]
	while True:
		if currentGroup[-1] - currentGroup[0] > max(wait):
			seats = seats - 
	
"""

def get_max_wait(cows, bus_num, capacity, start, end):
   if start == end:
      return 0
   elif start == end - 1:
      return 0
   elif end - start <= bus_num:
      return 0
   elif bus_num == 1 and end - start > capacity:
      print "hit"
      return -1
   elif bus_num == 1: 
      return cows[end-1] - cows[start]

   new_start = end - capacity
   if new_start <= start:
      new_start = start + 1

   current_min = -1
   for i in range(new_start, end):
      recur_min = get_max_wait(cows, bus_num - 1, capacity, start, i)
      if recur_min == -1:
         continue
      cur_group_min = cows[end-1] - cows[i]
      print recur_min, cur_group_min, "MINS"
      max_min = max(recur_min, cur_group_min)
      if current_min == -1:
         current_min = max_min
      elif current_min > max_min:
         current_min = max_min
   return current_min

in_file = open("convention.in", "r")
output = open("convention.out", "w")

info = map(int, in_file.readline().rstrip().split())
cowNum = info[0]
busNum = info[1]
capacity = info[2]

cows = map(int, in_file.readline().rstrip().split())
cows.sort()

answer = get_max_wait(cows, busNum, capacity, 0, cowNum)
output.write(str(answer) + "\n")
output.close()
