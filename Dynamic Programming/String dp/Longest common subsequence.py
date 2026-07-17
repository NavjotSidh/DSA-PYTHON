text1 = "abcde"
text2 = "ace"
m = len(text1)
n = len(text2)
def rec(i,j,text1,text2,dp):
    if i==m or j ==n:
        return 0
    if dp[i][j]!=0:
        return dp[i][j]
    if text1[i]==text2[j]:
        return 1 + rec(i+1,j+1,text1,text2,dp)
    else:
        one=rec(i+1,j,text1,text2,dp)
        two=rec(i,j+1,text1,text2,dp)
        dp[i][j]= max(one,two)
    return dp[i][j]
# def lcs(text1,text2):
#     dp=[[0 for j in range(n+1)] for i in range(m+1)]
#     return rec(0,0,text1,text2,dp)
# print(lcs(text1,text2))

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
print(lcs(text1,text2))