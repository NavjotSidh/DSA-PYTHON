from collections import deque
grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [1, 1, 1, 1, 0]
]
rows=len(grid)
cols=len(grid[0])
dist=[[float('inf')for _ in range(cols)]for _ in range(rows)]
q=deque()
q.append([1,0,0])
while q:
    dis,i,j=q.popleft()
    for x,y in ([1,0],[-1,0],[0,-1],[0,1],[1,1],[1,-1],[-1,-1],[-1,1]):
        new_i=x+i
        new_j=y+j
        if new_i<0 or new_i>=rows or new_j<0 or new_j>=cols:
            continue
        if grid[new_i][new_j]==1:
            continue
        new_dist=dis+1
        if new_dist<dist[new_i][new_j]:
            dist[new_i][new_j]=new_dist
            q.append([new_dist,new_i,new_j])
print(dist[rows-1][cols-1])