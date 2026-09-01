nums = [1, 1, 1]
k = 2
curr=0
map={0:1}
ans=0
for i in nums:
    curr+=i
    ans+=map.get(curr-k,0)
    map[curr]=map.get(curr,0)+1
print(ans)