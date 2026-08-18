arr = [1,2,3]
result=[]
total=0
def solve(ind,total):
    if ind>=len(arr):
        result.append(total)
        return
    total+=arr[ind]
    solve(ind+1,total)
    total-=arr[ind]
    solve(ind+1,total)
solve(0,0)
print(result)