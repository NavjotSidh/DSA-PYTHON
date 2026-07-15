#using recursion
arr=[5,3,1,8,6,2,9,4]
# def rec(nums,i):
#     if i>=len(nums):
#         return 0
#     #take case
#     take=nums[i]+rec(nums,i+2)
#
#     #not take
#     not_take=rec(nums,i+1)
#
#     return max(take,not_take)
# def house_rober(nums):
#     return rec(nums,0)
# print(house_rober(arr))

# using Memorization
def rec(nums,i,dp):
    if i>=len(nums):
        return 0

    if dp[i]!=-1:
        return dp[i]
    #take case
    take=nums[i]+rec(nums,i+2,dp)

    #not take
    not_take=rec(nums,i+1,dp)

    dp[i]= max(take,not_take)
    return dp[i]
def house_rober(nums):
    dp=[-1]*len(nums)
    return rec(nums,0,dp)

def house_robber2(nums):
    n = len(nums)
    if n == 1:
        return nums[0]

    no_last=house_rober(nums[:n-1])
    no_first=house_rober(nums[1:])
    return max(no_last,no_first)
print(house_robber2(arr))



# def house_rober(nums):
#     n=len(nums)
#     if n==1:
#         return nums[0]
#     dp=[0]*n
#     dp[0]=nums[0]
#     dp[1]=max(nums[0],nums[1])
#     for i in range(2,n):
#         dp[i]=max(nums[i]+dp[i-2],dp[i-1])
#     return dp[i]
# print(house_rober(arr))