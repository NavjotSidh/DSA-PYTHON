def minPathSum(grid):
    n = len(grid)
    m = len(grid[0])

    for j in range(1, m):
        grid[0][j] += grid[0][j - 1]

    for j in range(1, n):
        grid[j][0] += grid[j - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            top = grid[i - 1][j]
            left = grid[i][j - 1]

            grid[i][j] += min(top, left)
    return grid[n - 1][m - 1]
grid = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]
print(minPathSum(grid))