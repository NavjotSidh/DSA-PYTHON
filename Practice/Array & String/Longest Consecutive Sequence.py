nums = [100, 4, 200, 1, 3, 2]
map=set(nums)
ans=0
for i in nums:
    if i-1 not in map:
        curr=i
        length=1
        while curr+1 in map:
            curr+=1
            length+=1
        ans=max(ans,length)
print(ans)