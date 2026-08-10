arr = [1,3,4,6,6,6,6,8,9]
target = 6
l=0
r=len(arr)-1

while l<r:
    mid=(l+r)//2
    if arr[mid]>target:
        r=mid
    else:
        l=mid+1
print(l)