target=4
nums=[1,2,1,2,1]
nums.sort()
result=[]
def backtrack(ind,total,subset):
    if total==target:
        result.append(subset.copy())
        return
    if total>target:
        return
    if ind>=len(nums):
        return
    for i in range(ind,len(nums)):
        if i>ind and nums[i]==nums[i-1]:
            continue
        subset.append(nums[i])
        sum=total+nums[i]
        backtrack(i+1,sum,subset)
        subset.pop()
backtrack(0,0,[])
print(result)