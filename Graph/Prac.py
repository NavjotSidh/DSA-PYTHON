from collections import deque
adjList=[
    [1, 3, 5],
    [0, 2, 5],
    [1, 4],
    [0, 4],
    [0, 2, 3],
    [1]
]
visited=[False]*len(adjList)
q=deque()
q.append((1,-1))
visited[1]=True
ans=False
while len(q)>0:
    node,parent=q.popleft()
    for i in adjList[node]:
        if not visited[i]:
            visited[i]=True
            q.append((i,node))
        elif i!=parent:
            ans=True
            break
print(ans)