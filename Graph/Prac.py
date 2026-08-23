grid = [
    ["1","1","0","0","0"],
    ["1","1","0","1","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
    ["1","0","0","0","1"]
]

def solve(r,c):
    grid[r][c]="0"
    direction=[(0,1),(1,0),(-1,0),(0,-1)]
    for dr,dc in direction:
        nr=dr+r
        nc=dc+c
        if 0<=nr<rows and 0<=nc<cols and grid[nr][nc]=="1":
            solve(nr,nc)
    return

rows=len(grid)
cols=len(grid[0])
ans=0
for i in range(rows):
    for j in range(cols):
        if grid[i][j]=="1":
            ans+=1
            solve(i,j)
print(ans)