adjList=[
    [1, 3, 5],
    [0, 2, 5],
    [1, 4],
    [0, 4],
    [0, 2, 3],
    [1]
]
visited=[False]*len(adjList)

def dfs(node,parent):
    visited[node]=True
    for i in adjList[node]:
        if not visited[i]:
            ans=dfs(i,node)
            if ans==True:
                return True
        elif i!=parent:
            return True
    return False
print(dfs(1,-1))