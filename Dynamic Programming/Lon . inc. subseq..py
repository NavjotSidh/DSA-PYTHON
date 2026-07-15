def rec(i,prev,nums,dp):
    if i >= len(nums):
        return 0

    take=0
    if dp[i][prev+1]!=-1:
        return dp[i][prev+1]
    #take case
    if prev == -1 or nums[prev] < nums[i]:
        take=1+rec(i+1,i,nums,dp)
    #not take case
    not_take=rec(i+1,prev,nums,dp)

    dp[i][prev+1]=max(take,not_take)
    return dp[i][prev+1]


nums=[10,9,2,5,3,7,101,18]
def lon_inc(nums):
    dp=[[-1 for i in range(len(nums)+1)] for j in range(len(nums))]
    return rec(0,-1,nums,dp)
print(lon_inc(nums))