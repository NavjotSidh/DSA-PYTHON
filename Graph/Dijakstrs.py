from heapq import heappop,heappush
adjList=[
    [(2,4),(1,4)],
    [(0,4),(2,2)],
    [(0,4),(1,2),(3,3),(5,6),(4,1)],
    [(2,3),(5,2)],
    [(2,1),(5,3)],
    [(3,2),(2,6),(4,3)]
]
dist=[float('inf')]*6
heap=[]
dist[0]=0
heappush(heap,(dist[0],0))
while len(heap)>0:
    d,u=heappop(heap)
    for i in adjList[u]:
        if dist[u]+i[1] < dist[i[0]]:
            dist[i[0]]=(dist[u]+i[1])
            heappush(heap,(dist[i[0]],i[0]))
print(dist)