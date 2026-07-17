grid=[[0,0,0],[0,0,1],[0,0,0]]
def rec(i,j,grid,dp):
    m=len(grid)
    n=len(grid[0])
    if i>=m or j>=n:
        return 0
    if grid[i][j]==1:
        return 0
    if i==m-1 and j==n-1 :
        return 1
    if dp[i][j]!=-1:
        return dp[i][j]
    right=rec(i,j+1,grid,dp)
    bottom=rec(i+1,j,grid,dp)
    dp[i][j]=right+bottom
    return dp[i][j]
# def unique_path_II(grid):
#     m=len(grid)
#     n=len(grid[0])
#     dp=[[-1 for i in range(n+1)] for j in range(m+1)]
#     return rec(0,0,grid,dp)
# print(unique_path_II(grid))

def unique_path_II(grid):
    m=len(grid)
    n=len(grid[0])
    dp=[[-1 for i in range(n+1)] for j in range(m+1)]
    dp[m-1][n-1]=1
    if grid[m-1][n-1] == 1:
        return 0

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if grid[i][j]==1:
                dp[i][j]=0
                continue
            if i ==m-1 and j ==n-1:
                continue
            right=0
            bottom=0
            if i+1<m:
                bottom=dp[i+1][j]
            if j+1<n:
                right=dp[i][j+1]

            dp[i][j]=right+bottom
    return dp[0][0]
print(unique_path_II(grid))