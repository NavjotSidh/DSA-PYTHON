# def fib(n):
#     if n==0 or n==1:
#         return n
#     dp=[-1]*(n+1)
#     dp[0]=0
#     dp[1]=1
#     for i in range(2,n+1):
#         dp[i]=dp[i-1]+dp[i-2]
#     return dp[n]
# print(fib(6))

#Optimal solution(SC=O(1))
def fib(n):
    if n==0 or n==1:
        return n
    a=0
    b=1
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c

    return b
print(fib(6))