adjList=[
    [1, 3, 5],
    [0, 2, 5],
    [1, 4],
    [0, 4],
    [0, 2, 3],
    [1]
]
visited=[False]*len(adjList)
def detect(i,parent):
    visited[i]=True
    for x in adjList[i]:
        if x==parent:
            continue
        if  visited[x]:
            return True
        if detect(x,i):
            return True
    return False
print(detect(0,-1))