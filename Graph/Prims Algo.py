adjmatrix = [
    [0, 9, 75, 0, 0],
    [9, 0, 95, 19, 42],
    [75, 95, 0, 51, 66],
    [0, 19, 51, 0, 31],
    [0, 42, 66, 31, 0]
]
ans=0
n=len(adjmatrix)
visited=[False]*n
visited[0]=True
for e in range(n-1):
    x=-1
    y=-1
    mn=float('inf')
    for i in range(n):
        for j in range(n):
            if adjmatrix[i][j]!=0 and visited[i] and not visited[j]:
                if adjmatrix[i][j]<mn:
                    mn=adjmatrix[i][j]
                    x = i
                    y = j
    visited[y]=True
    ans+=mn
print(ans)