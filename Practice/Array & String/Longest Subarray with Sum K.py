nums = [10, 5, 2, 7, 1, 9]
k = 15
ans=0
total=0
start=0
for i,num in enumerate(nums):
    total+=num
    while total>k:
        total-=nums[start]
        start+=1
    if total==k:
        ans=max(ans,(i-start)+1)
print(ans)
