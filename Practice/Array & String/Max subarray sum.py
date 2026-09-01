nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
curr=nums[0]
best=nums[0]
for i in nums[1:]:
    curr=max(curr,curr+i)
    best=max(best,curr)
print(best)