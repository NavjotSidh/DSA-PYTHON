word1="sea"
word2="eat"
m = len(word1)
n = len(word2)
def lcs(text1,text2):
    dp=[[0 for j in range(n+1)] for i in range(m+1)]
    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if text1[i]==text2[j]:
                dp[i][j]=1+ dp[i+1][j+1]
            else:
                one= dp[i+1][j]
                two= dp[i][j+1]
                dp[i][j]=max(one,two)
    return dp[0][0]

print((m+n)-2*lcs(word1,word2))