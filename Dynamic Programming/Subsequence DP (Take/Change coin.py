def rec(i,sm,arr,amount,dp):
    if i == len(arr):
        return float('inf')
    if sm>amount:
        return float('inf')
    if sm==amount:
        return 0
    if dp[i][sm]!=-1:
        return dp[i][sm]

    #take
    take=1+rec(i,sm+arr[i],arr,amount,dp)

    #not take
    not_take=rec(i+1,sm,arr,amount,dp)

    dp[i][sm]=min(take,not_take)
    return  dp[i][sm]
def change_coin(arr,amount):
    n=len(arr)
    dp = [[-1] * (amount + 1) for _ in range(n)]

    return rec(0,0,arr,amount,dp)

print(change_coin([1,2,5],11))