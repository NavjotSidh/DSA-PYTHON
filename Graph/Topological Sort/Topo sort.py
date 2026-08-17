adjList = [
    [1, 2],    # 0 → 1, 2
    [3],       # 1 → 3
    [3],       # 2 → 3
    [4],       # 3 → 4
    []         # 4
]
x=len(adjList)
visited=[False]*x
stack=[]

def dfs(node):
    visited[node]=True
    for i in adjList[node]:
        if not visited[i]:
            dfs(i)
    stack.append(node)


for i in range(0, x):
    if not visited[i]:
        dfs(i)
print(stack[::-1])