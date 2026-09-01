nums = [1, 1, 1, 3, 3, 2, 2, 2]
n=len(nums)
map={}
ans=[]
for i in nums:
    map[i]=map.get(i,0)+1
    if map.get(i,0)>n/3 and i not in ans:
        ans.append(i)
print(ans)