nums = [100, 4, 200, 1, 3, 2]
seen=set(nums)
res=[]
for i in nums:
    ans=[]
    if i-1 not in seen:
        ans.append(i)
        while i+1 in seen:
            ans.append(i+1)
            i+=1
        if len(ans)>len(res):
            res=ans
print(res)