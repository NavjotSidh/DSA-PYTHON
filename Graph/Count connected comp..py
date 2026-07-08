adjMatrix = [
    [0,1,0,0,0,0,0,0],  # 0
    [1,0,0,0,0,1,0,0],  # 1
    [0,0,0,1,1,0,1,0],  # 2
    [0,0,1,0,1,0,0,0],  # 3
    [0,0,1,1,0,0,0,0],  # 4
    [0,1,0,0,0,0,0,0],  # 5
    [0,0,1,0,0,0,0,0],  # 6
    [0,0,0,0,0,0,0,0]   # 7
]
adjList2=[
    [4,3],
    [2],
    [1],
    [0],
    [0]
]
adjList3 = [
    [1],        # 0
    [0,5],      # 1
    [3,4,6],    # 2
    [2,4],      # 3
    [2,3],      # 4
    [1],        # 5
    [2],        # 6
    []          # 7
]
n=len(adjMatrix)
visited=[False]*n
def dfs(i,adjMatrix,visited):
    visited[i]=True
    for x in range(len(adjMatrix)):
        if adjMatrix[i][x] and not visited[x]:
            dfs(x,adjMatrix,visited)
ans=0
for i in range(n):
    if not visited[i]:
        dfs(i,adjMatrix,visited)
        ans+=1
print(ans)