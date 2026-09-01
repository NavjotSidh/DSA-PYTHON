nums = [1, 0, -1, 0, -2, 2]
n=len(nums)
target = 0
nums.sort()
ans=[]

for i in range(n):
    for j in range(i+1,n):
        comp=target-nums[i]-nums[j]
        l=j+1
        r=n-1
        while l<r:
            if nums[l]+nums[r]==comp:
                ans.append([nums[i],nums[j],nums[l],nums[r]])
                l+=1
                r-=1
            elif nums[l]+nums[r]<comp:
                l+=1
            elif nums[l]+nums[r]>comp:
                r-=1
print(ans)