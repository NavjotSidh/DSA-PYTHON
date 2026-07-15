def rec(n,dp):
    dp=[-1]*(n+1)
    if n==0 or n==1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=rec(n-1,dp) + rec(n-2,dp)
    return dp[n]
def fib(n):
    dp=[-1]*(n+1)
    return rec(n,dp)
print(fib(6)) 