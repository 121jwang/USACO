from collections import defaultdict 
   
#This class represents a directed graph  
# using adjacency list representation 
class Graph: 
   
    def __init__(self,vertices): 
        #No. of vertices 
        self.V= vertices  
          
        # default dictionary to store graph 
        self.graph = defaultdict(list)  
   
    # function to add an edge to graph 
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
   
    '''A recursive function to print all paths from 'u' to 'd'. 
    visited[] keeps track of vertices in current path. 
    path[] stores actual vertices and path_index is current 
    index in path[]'''
    def printAllPathsUtil(self, u, d, visited, path, cpath): 
  
        # Mark the current node as visited and store in path 
        visited[u]= True
        path.append(u) 
  
        # If current vertex is same as destination, then print 
        # current path[] 
        if u == d:
            cpath.append(list(path))
            path.pop()
            visited[u] = False
            return cpath 
        else: 
            # If current vertex is not destination 
            #Recur for all the vertices adjacent to this vertex 
            for i in self.graph[u]: 
                if visited[i]==False: 
                    cpath = self.printAllPathsUtil(i, d, visited, path, cpath) 
                      
        # Remove current vertex from path[] and mark it as unvisited 
        path.pop() 
        visited[u]= False
        
        return cpath
   
    # Prints all paths from 's' to 'd' 
    def printAllPaths(self,s, d): 
  
        # Mark all the vertices as not visited 
        visited =[False]*(self.V) 
  
        # Create an array to store paths 
        path = [] 
  
        # Call the recursive helper function to print all paths 
        return self.printAllPathsUtil(s, d,visited, path, []) 


in_file = open("closing.in", "r")
output = open("closing.out", "w")

barnNum, paths = map(int, in_file.readline().split())

barns = Graph(barnNum)

for i in range(paths):
    connect = map(int, in_file.readline().split())
    barns.addEdge(connect[0] - 1, connect[1] - 1)
    barns.addEdge(connect[1] - 1, connect[0] - 1)

## Find the last removed barn
deleteOrder = []
for x in range(barnNum):
    deleteOrder.append(int(in_file.readline()) - 1)

## Base connections off of the last removed barn
startNode = deleteOrder[-1]

toBarn = []
for i in range(barnNum):
    toBarn.append(barns.printAllPaths(startNode, i))




