arr=[2,3,6,7]
target=7
result=[]
def solve(ind,total,subset):
    if total==target:
        result.append(subset.copy())
        return
    if ind>=len(arr):
        return
    if total>target:
        return
    subset.append(arr[ind])
    sum=total+arr[ind]
    solve(ind,sum,subset)
    sum=total
    subset.pop()
    solve(ind+1,sum,subset)
solve(0,0,[])
print(result)