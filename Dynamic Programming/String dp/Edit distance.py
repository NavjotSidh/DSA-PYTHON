word1="horse"
word2="ros"
m=len(word1)
n=len(word2)
def rec(i,j,dp):
    if i==m :
        return n-j
    if j==n:
        return m-i
    if dp[i][j]!=-1:
        return dp[i][j]
    if word1[i]==word2[j]:
        return rec(i+1,j+1,dp)
    else:
        insert=1+rec(i,j+1,dp)
        delete=1+rec(i+1,j,dp)
        replace=1+rec(i+1,j+1,dp)

    dp[i][j]=min(insert,delete,replace)
    return dp[i][j]
def edit_distance(word1,word2):
    dp=[[-1 for j in range(n+1)]for i in range(m+1)]
    return rec(0,0,dp)
print(edit_distance(word1,word2))

def minDistance(word1, word2):

    m = len(word1)
    n = len(word2)

    dp = [[0 for _ in range(n+1)]
          for _ in range(m+1)]

    # Base cases
    for i in range(m+1):
        dp[i][n] = m - i

    for j in range(n+1):
        dp[m][j] = n - j

    for i in range(m-1, -1, -1):
        for j in range(n-1, -1, -1):

            if word1[i] == word2[j]:
                dp[i][j] = dp[i+1][j+1]
            else:
                insert = dp[i][j+1]
                delete = dp[i+1][j]
                replace = dp[i+1][j+1]

                dp[i][j] = 1 + min(insert, delete, replace)

    return dp[0][0]

