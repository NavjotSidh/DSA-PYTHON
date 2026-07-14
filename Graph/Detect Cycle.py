adjList=[
    [1,3,5],
    [0,2,5],
    [1,4],
    [0,4],
    [0,2,3],
    [1]
]
adjList2=[
    [1,3],
    [0,2],
    [1],
    [0],
    [0]
]
n=len(adjList)
visited=[False]*n
def detect(i,parent,adjList,visited):
    visited[i]=True
    for x in adjList[i]:
        if x==parent:
            continue
        if visited[x]:
            return True
        if detect(x,i, adjList, visited):
            return True
    return False
print(detect(0,-1,adjList2,visited))