edges=[(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]
n=6   #Nodes
e=7   #Edges
adjList=[]
for i in range(n):
    adjList.append([])
for edge in edges:
    x=edge[0]
    y=edge[1]
    adjList[x].append(y)
    adjList[y].append(x)

ans=[]
visited=[False]*n
def dfs(i,adjList,visited):
    ans.append(i)
    visited[i]=True
    for x in adjList[i]:
        if not visited[x]:
            dfs(x,adjList,visited)

dfs(0,adjList,visited)
print(ans)