def rec(i,cost,dp):
    if i >= len(cost):
        return 0

    if dp[i]!=-1:
        return dp[i]
    #take
    take=rec(i+2,cost,dp)

    #not take
    not_take=rec(i+1,cost,dp)
    dp[i]=cost[i]+min(take,not_take)
    return dp[i]

def climb(cost):
    dp=[-1]*len(cost)
    return min(rec(0,cost,dp),rec(1,cost,dp))
# print(climb([10, 15, 20]))

#Tabulation (Bottom-Up)
def climb_tab(cost):
    n=len(cost)
    dp=[0]*(n+2)
    for i in range(n-1,-1,-1):
        dp[i]=cost[i]+min(dp[i+1],dp[i+2])
    return min(dp[0],dp[1])
print(climb_tab([10,15,20]))