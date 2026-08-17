import heapq
adj = {
    0: [(1, 4), (2, 1)],
    1: [(0, 4), (2, 2), (3, 5)],
    2: [(0, 1), (1, 2), (3, 8), (4, 10)],
    3: [(1, 5), (2, 8), (4, 2)],
    4: [(2, 10), (3, 2)]
}
dist=[float('inf')]*len(adj)
parent=[i for i in range(len(adj))]
priority_queue=[]
priority_queue.append([0,0])
dist[0]=0

while priority_queue:
    d,node=heapq.heappop(priority_queue)
    for i,wt in adj[node]:
        dist_trav=d+wt
        if dist_trav<dist[i]:
            dist[i]=dist_trav
            heapq.heappush(priority_queue,[dist_trav,i])
            parent[i]=node
path=[]
n=len(adj)-1
while parent[n]!=n:
    path.append(n)
    n=parent[n]
path.append(0)
print(path[::-1])