nums = [1, 2, 3]
ans=[]
def backtrack(i,subset):
    if i==len(nums):
        ans.append(subset.copy())
        return
    #take
    subset.append(nums[i])
    backtrack(i+1,subset)

    #not_take
    subset.pop()
    backtrack(i+1,subset)
    return ans
print(backtrack(0,[]))