in_file = open("rental.in", "r")
output = open("rental.out", "w")

info = map(int, in_file.readline().split())
cowNum = info[0]
storeNum = info[1]
neighborNum = info[2]

cows = []
for x in range(cowNum):
    cows.append(int(in_file.readline()))
cows = sorted(cows)

stores = []
for x in range(storeNum):
    stores.append(map(int, in_file.readline().split()))
stores = sorted(stores, key = lambda x: x[1], reverse = True)

neighbors = []
for x in range(storeNum):
    neighbors.append(int(in_file.readline()))
neighbors = sorted(neighbors, reverse = True)

print cows
print stores
print neighbors

storePos = 0
neighborPos = 0

profit = 0
for cow in cows:
    ## Find how much you'd make by selling milk
    sellMilk = 0
    
    startStorePos = storePos
    cowsPer = []
    while True:
        cowsPer.append(stores[storePos][0])
        if stores[storePos][0] >= cow:
            sellMilk = sellMilk + cow * stores[storePos][1]
            stores[storePos][0] = stores[storePos][0] - cow
            if stores[storePos][0] == 0:
                storePos = storePos + 1
            break
        else:
            sellMilk = sellMilk + stores[storePos][0] * stores[storePos][1]
            cow = cow - stores[storePos][0]
            storePos = storePos + 1
    
    print sellMilk
    ## If selling milk is worthwhile
    if sellMilk > neighbors[neighborPos]:
        print "Cow: " + str(cow) + " SELL MILK"
        profit = profit + sellMilk
    else:
        print "Cow: " + str(cow) + " RENT COW"
        profit = profit + neighbors[neighborPos]
        neighborPos = neighborPos + 1
        for x in range(len(cowsPer)):
            stores[x + startStorePos][0] = cowsPer[x]
        storePos = startStorePos

    print stores

print profit
