adjList = [
    [1, 2],    # 0 → 1, 2
    [0, 2],    # 1 → 0, 2
    [0, 1, 3], # 2 → 0, 1, 3
    [2]        # 3 → 2
]
visited=[-1]*len(adjList)
def dfs(curr,color):
    visited[curr]=color
    for i in adjList[curr]:
        if visited[i] != -1:
           if visited[i]==color:
               return False
        else:
            x=dfs(i,1-color)
            if x==False:
                return False
    return True
print(dfs(0,0))