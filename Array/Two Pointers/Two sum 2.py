nums = [2,2,5,7,11,15]
target = 9
n=len(nums)
ans=0
l=0
r=n-1
while l<r:
    sum=nums[l]+nums[r]
    if sum==target:
        ans=(l,r)
        break
    elif sum<target:
        l+=1
    else:
        r-=1
print(ans)