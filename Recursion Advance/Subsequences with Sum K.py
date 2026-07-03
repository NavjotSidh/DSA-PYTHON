nums=[5,9,3,1,4]
result = []
target=9
def solve(ind,sum,subset):
    if sum==target:
        result.append(subset.copy())
        return
    elif sum>target:
        return
    if ind>=len(nums):
        return
    subset.append(nums[ind])
    sum+=nums[ind]
    solve(ind+1,sum,subset)
    e=subset.pop()
    sum-=e
    solve(ind+1,sum,subset)
solve(0,0,[])
print(result)
