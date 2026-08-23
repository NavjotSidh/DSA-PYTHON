def arrayManipulation(n, queries):
    # Write your code here
    arr=[0]*(n+1)
    for a,b,k in queries:
        arr[a-1]+=k
        arr[b]-=k
    curr=0
    best=float('-inf')
    for i in arr:
        curr+=i
        best=max(best,curr)
    return best