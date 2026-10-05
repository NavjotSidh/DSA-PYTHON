m = 3
n = 3

def rec(i,j,m,n,dp):
    if i>=m or j>=n :
        return 0
    if i==m-1 and j==n-1:
        return 1
    if dp[i][j] != -1:
        return dp[i][j]

    right=rec(i+1,j,m,n,dp)
    down=rec(i,j+1,m,n,dp)
    dp[i][j]=right+down
    return dp[i][j]

def unique_path(m,n):
    dp=[[-1 for _ in range(n+2)] for _ in range(m+2)]
    return rec(0,0,m,n,dp)
print(unique_path(m,n))