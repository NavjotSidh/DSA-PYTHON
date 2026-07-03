arr = [1,3,4,4,6,8,7,9]
target = 5
l=0
r=len(arr)-1
ans=len(arr)
while l<=r:
    mid=(l+r)//2
    if arr[mid]>=target:
        ans=mid
        r=mid-1
    else:
        l=mid+1
print(ans)