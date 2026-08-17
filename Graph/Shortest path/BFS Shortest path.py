from collections import deque

adj = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3, 4],
    3: [1, 2, 5],
    4: [2, 5],
    5: [3, 4]
}
q=deque()
dist=[-1]*len(adj)
dist[0]=0
q.append([0,0])
while q:
    node,dis=q.popleft()
    for i in adj[node]:
        if dist[i]==-1:
            dist[i]=dis+1
            q.append([i,dis+1])
print(dist)