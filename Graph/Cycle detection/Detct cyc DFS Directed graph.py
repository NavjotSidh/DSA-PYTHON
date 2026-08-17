adjList = [
    [1],       # 0 → 1
    [2],       # 1 → 2
    [3],       # 2 → 3
    [1, 4],    # 3 → 1, 4
    []         # 4
]
visited=[False]*len(adjList)
path_visited=[False]*len(adjList)
def dfs(curr):
    visited[curr]=True
    path_visited[curr]=True
    for i in adjList[curr]:
        if not visited[i]:
            x=dfs(i)
            if x==True:
                return True
        elif path_visited[i]==True:
            return True
    path_visited[curr]=False
    return False
print(dfs(0))