def rec(i,sm,nums,target,dp):
    total=sum(nums)
    if sm==target and i==len(nums):
        return 1
    if i>=len(nums):
        return 0
    if dp[i][sm + total]!= -1:
        return dp[i][sm+total]
    pos=rec(i+1,sm+nums[i],nums,target,dp)
    neg=rec(i+1,sm-nums[i],nums,target,dp)
    dp[i][sm + total]=pos + neg
    return dp[i][sm + total]

def target_sum(nums,target):
    dp=[[-1 for j in range(2*sum(nums)+1)] for i in range(len(nums))]
    return rec(0,0,nums,target,dp)
print(target_sum([1,1,1,1,1],3))