nums = [1, 2, 2]
nums.sort()
ans=[]
def backtrack(start,subset):
    ans.append(subset.copy())
    for i in range(start,len(nums)):
        if i>start and nums[i]==nums[i-1]:
            continue
        subset.append(nums[i])
        backtrack(i+1,subset)
        subset.pop()
    return ans
print(backtrack(0,[]))