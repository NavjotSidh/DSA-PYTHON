#Bounded / 1-0 Knapsack
value=[10,5,8,5,3]
weight=[3,2,4,6,4]
W=6
n=len(value)

def knapsack(i,W,n,value,weight,dp):
    if i>=n:
        return 0

    if dp[i]!= -1:
        return dp[i][W]
    take=0
    #Take
    if weight[i]<=W:
        take=value[i]+knapsack(i+1,W-weight[i],n,value,weight,dp)

    #not take
    no_take=knapsack(i+1,W,n,value,weight,dp)
    dp[i][W]= max(take,no_take)
    return dp[i][W]

def sol(value, weight):
    dp = [[-1] * (W + 1) for _ in range(n)]
    return knapsack(0, W, n, value, weight, dp)

print(sol(value,weight))