def countTriplets(arr, r):
    left={}
    right={}
    ans=0
    for i in arr:
        right[i]=right.get(i,0)+1
    for x in arr:
        right[x]-=1
        if x%r==0:
            a=x//r
            b=x*r
            ans+=left.get(a,0) * right.get(b,0)
        left[x]=left.get(x,0)+1
    return ans
arr = [1,1,1,1,2,2,2,4,4,4]
r = 2
print(countTriplets(arr,r))