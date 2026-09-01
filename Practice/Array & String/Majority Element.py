nums = [3, 2, 3]
n=len(nums)
map={}
for i in nums:
    map[i]=map.get(i,0)+1
    if map.get(i,0)>n/2:
        print(i)
        break