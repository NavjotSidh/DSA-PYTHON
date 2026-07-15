def rec(i,j,text1,text2,dp):
    if i>=len(text1) or j>=len(text2):
        return 0
    ans=0
    if dp[i][j] !=-1:
        return dp[i][j]
    if text1[i]==text2[j]:
        dp[i][j]= 1+rec(i+1,j+1,text1,text2,dp)
        return dp[i][j]
    else:
        first=rec(i+1,j,text1,text2,dp)
        second=rec(i,j+1,text1,text2,dp)
        dp[i][j]=max(first,second)
        return dp[i][j]

def longest_subsequence(text1,text2):
    dp=[[-1 for i in range(len(text2))] for j in range(len(text1))]
    return rec(0,0,text1,text2,dp)
print(longest_subsequence("abefaghi","bfajeho"))