Grid =[
["1","0","1","0","1"],
["0","0","0","0","0"],
["1","1","0","1","0"],
["0","0","0","0","1"],
["1","0","0","0","1"]
]

def dfs(r,c,grid):
    row = len(grid)
    col = len(grid[0])

    if r < 0 or r >= row or c < 0 or c >= col or grid[r][c] == "0":
        return
    grid[r][c] = "0"
    dfs(r + 1, c, grid)
    dfs(r - 1, c, grid)
    dfs(r, c + 1, grid)
    dfs(r, c - 1, grid)


def numIslands(grid) :
    row = len(grid)
    col = len(grid[0])
    ans = 0
    for r in range(row):
        for c in range(col):
            if grid[r][c] == "1":
                ans += 1
                dfs(r, c, grid)
    return ans
print(numIslands(Grid))