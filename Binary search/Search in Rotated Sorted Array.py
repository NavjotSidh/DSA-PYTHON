arr=[4,5,6,7,0,1,2]
target=2
l=0
r=len(arr)-1
while l<=r:
    mid=(l+r)//2
    if arr[mid]==target:
        print(mid)
    if arr[l] <= arr[mid]:
        if arr[l] <= target < arr[mid]:
            r=mid-1
        else:
            l=mid+1
    else:
        if arr[mid] < target <= arr[r]:
            l=mid+1
        else:
            r=mid-1