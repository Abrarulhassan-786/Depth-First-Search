#-----DEPTH FIRST SEARCH ALGORITHM----
#---ABRAR UL HASSAN SPJ---------
graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}
visited = set() #Set to keep track of visited nodes of paragraph
print(visited)
def dfs(visited,graph,node): #function for dfs
    if node not in visited:
        print(node,end=" ")
        visited.add(node)
        #print("visited ",visited)
        for neighbour in graph[node]:
            #print("neighbour value ",neighbour)
            dfs(visited,graph,neighbour) #recursive function
#Driver Code
dfs(visited,graph,'5')