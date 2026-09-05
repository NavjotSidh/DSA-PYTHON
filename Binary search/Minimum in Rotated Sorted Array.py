arr=[4,5,6,0,1,
     7,2]
target=2
l=0
r=len(arr)-1
ans=arr[0]
while l<=r:
    mid=(l+r)//2
    if arr[l]<=arr[mid]:
        ans=min(arr[l],ans)
        l=mid+1
    else:
        ans=min(ans,arr[mid])
        r=mid-1
print(ans)