nums = [1, 2, 3]
used=[False]*len(nums)
ans=[]
def backtracking(path,used):
    if len(path)==len(nums):
        ans.append(path.copy())
        return
    for i in range(len(nums)):
        if used[i]:
            continue
        used[i]=True
        path.append(nums[i])
        backtracking(path,used)
        path.pop()
        used[i]=False
used=[False]*len(nums)
backtracking([],used)
print(ans)