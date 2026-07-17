def rec(a,b,m,n,dp):
    if a==m-1 or b==n-1:
        return 1
    if a >= m or b >= n:
        return 0
    if dp[a][b]!=-1:
        return dp[a][b]
    right=rec(a,b+1,m,n,dp)

    bottom=rec(a+1,b,m,n,dp)
    dp[a][b]=right + bottom
    return dp[a][b]
# def unique_path(m,n):
#     dp=[[-1 for i in range(n+1)] for j in range(m+1)]
#     return rec(0,0,m,n,dp)
#
# print(unique_path(3,4))

#Tabulation (Bottom-Up)
def unique_path(m,n):
    dp=[[-1 for i in range(n+1)] for j in range(m+1)]
    dp[m-1][n-1]=1
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i==m-1 and j==n-1:
                continue
            down=0
            right=0

            if i+1 <m :
                down=dp[i+1][j]
            if j+1<n:
                right=dp[i][j+1]
            dp[i][j]=down+right
    return dp[0][0]
print(unique_path(3,4))