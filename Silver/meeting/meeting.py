from collections import defaultdict 

class Graph: 
    paths = []
    def __init__(self, vertices):  
        self.V= vertices  
        self.graph = defaultdict(list)  

    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    def printAllPathsUtil(self, u, d, visited, path): 
        visited[u]= True
        path.append(u) 

        if u == d: 
            #print path
            self.paths.append(list(path))
        else: 
            for i in self.graph[u]:
                if not visited[i]: 
                    self.printAllPathsUtil(i, d, visited, path) 
                      
        path.pop() 
        visited[u] = False
   
    def getPaths(self, s, d): 
        visited =[False]*(self.V) 
        path = [] 
        self.printAllPathsUtil(s, d,visited, path) 

        return self.paths

inFile = open("meeting.in", "r")
output = open("meeting.out", "w")

fieldCount, pathCount = map(int, inFile.readline().split())

costs = {}
g = Graph(fieldCount)


for i in range(pathCount):
    info = map(int, inFile.readline().split())

    g.addEdge(info[0] - 1, info[1] - 1)
    costs[(info[0] - 1, info[1] - 1)] = (info[2], info[3])

bessieCosts = []
elsieCosts  = []

paths = g.getPaths(0, fieldCount - 1)

for path in paths:
    bCost = 0
    eCost = 0
    for x in range(0, len(path) - 1):
        bCost = bCost + costs[(path[x], path[x + 1])][0]
        eCost = eCost + costs[(path[x], path[x + 1])][1]
    bessieCosts.append(bCost)
    elsieCosts.append(eCost)

#print bessieCosts
#print elsieCosts

elsieSet = set(elsieCosts)

minCost = next((a for a in bessieCosts if a in elsieSet), None)
print minCost

if minCost == None:
    minCost = "IMPOSSIBLE"
output.write(str(minCost) + "\n")
output.close()