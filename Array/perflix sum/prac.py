# nums = [1,2,3,4]
# ans=[0]*len(nums)
#
# prefix=1
# for i in range(len(nums)):
#     ans[i]=prefix
#     prefix=nums[i]*prefix
#
# suffix=1
# for i in range(len(nums)-1,-1,-1):
#     ans[i]*=suffix
#     suffix=nums[i]*suffix

nums = [-2,1,-3,4,-1,2,1,-5,4]
currmax=nums[0]
best=nums[0]
for i in nums:
    currmax=max(currmax+i,i)
    best=max(best,currmax)
print(best)