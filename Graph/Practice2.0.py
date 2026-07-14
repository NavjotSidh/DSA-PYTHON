from heapq import heappop,heappush
class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1

    def push(self,x):
        if self.front==-1:
            self.front=0
        self.q.append(x)
    def pop(self):
        if len(self.q) == 0:
            return -1
        return self.q.pop(0)
    def getFront(self):
        if len(self.q)==0:
            return -1
        return self.q[self.front]
    def size(self):
        return len(self.q)-self.front

#shortest path algo
#Dijakstra
# adjList=[
#     [(2,4),(1,4)],  #0
#     [(0,4),(2,2)],  #1
#     [(0,4),(1,2),(3,3),(5,6),(4,1)],    #2
#     [(2,3),(5,2)],  #3
#     [(2,1),(5,3)],  #4
#     [(3,2),(2,6),(4,3)] #5
# ]
# adjmatrix = [
#     [0, 9, 75, 0, 0],
#     [9, 0, 95, 19, 42],
#     [75, 95, 0, 51, 66],
#     [0, 19, 51, 0, 31],
#     [0, 42, 66, 31, 0]
# ]
# n=len(adjList)
# l=len(adjmatrix)
# # def dijakstra(i,adjList):
# #     heap=[]
# #     dist=[float('inf')]*n
# #     dist[i]=0
# #     heappush(heap,(dist[i],i))
# #     while len(heap)>0:
# #         d, u = heappop(heap)
# #
# #         if d > dist[u]:
# #             continue
# #         for v,w in adjList[u]:
# #             if dist[u]+w<dist[v]:
# #                 dist[v]=dist[u]+w
# #                 heappush(heap,(dist[v],v))
# #     return dist
# # print(dijakstra(0,adjList))
#
# #prims algo


def Prims(start,adjmatrix):
    visited=[False]*n
    ans=0
    visited[start]=True
    for a in range(l-1):
        x=-1
        y=-1
        mn=float('inf')
        for i in range(l):
            for j in range(l):
                if adjmatrix[i][j]!=0 and visited[i] and not visited[j]:
                    if adjmatrix[i][j]<mn:
                        mn=adjmatrix[i][j]
                        x=i
                        y=j
        visited[y]=True
        ans+=mn
    return ans
# print(Prims(0,adjmatrix))


#kahn algo
adjList = [
    [1, 3, 4],    # 0
    [],       # 1
    [],          # 2
    [2],    # 3
    [1, 3]     # 4
]
def kahn(adjList):
    n=len(adjList)
    q=Queue()
    indegree=[0]*n
    ans=[]
    for i in range(n):
        for j in adjList[i]:
            indegree[j]+=1
    for i in range(n):
        if indegree[i]==0:
          q.push(i)
    while q.size()>0:
        front=q.pop()
        ans.append(front)

        for i in adjList[front]:
            indegree[i]-=1
            if indegree[i]==0:
                q.push(i)
    return ans
print(kahn(adjList))