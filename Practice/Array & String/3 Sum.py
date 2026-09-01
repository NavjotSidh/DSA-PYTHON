nums = [3, -2, -1, 0, 1, 2, -3]
target = 0
nums.sort()
ans=[]

for i,num in enumerate(nums):
    comp=target-num
    l=i+1
    r=len(nums)-1
    while l<r:
        if nums[l]+nums[r]==comp:
            ans.append([num,nums[l],nums[r]])
            l+=1
            r-=1
        elif nums[l]+nums[r]<comp:
            l+=1
        elif nums[l]+nums[r]>comp:
            r-=1
print(ans)