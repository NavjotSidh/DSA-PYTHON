arr = [1,3,4,4,5,6,6,8,7,9]
target = 4
l=0
r=len(arr)-1
ans=len(arr)
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target:
        ans=mid
        l=mid+1
    elif arr[mid]<target:
        l=mid+1
    else:
        r=mid-1
print(ans)