nums=[10,9,2,5,3,7,101,18,5]
n=len(nums)

# def rec(i,prev,dp):
#     if i>=n:
#         return 0
#     if dp[i][prev]!=-1:
#         return dp[i][prev]
#     if prev==-1 or  nums[i]>nums[prev]:
#         take=1+rec(i+1,i,dp)
#         not_take=rec(i+1,prev,dp)
#         dp[i][prev]=max(take,not_take)
#         return dp[i][prev]
#     return 0
def lis(nums):

    dp=[[0 for j in range(n+1)]for i in range(n+1)]
    for i in range(n-1,-1,-1):
        for prev in range(i-1,-2,-1):
            take=0
            if prev == -1 or nums[i] > nums[prev]:
                take=1+dp[i+1][i+1]
            not_take=dp[i+1][prev+1]
            dp[i][prev+1]=max(take,not_take)
    return dp[0][0]
print(lis(nums))