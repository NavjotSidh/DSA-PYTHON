nums = [1,2,3,4]
ans=[0]*len(nums)
for i in range(len(nums)):
    product=1
    for j in range(len(nums)):
        if i!=j:
            product*=nums[j]
        ans[i]=product
print(ans)