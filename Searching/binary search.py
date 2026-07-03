arr = [1,3,4,5,6,8,7,9]
target = 5
l=0
r=len(arr)-1
while l<=r:
    mid=l+r//2
    if arr[mid]==target:
        print(mid)
        break
    elif arr[mid]<target:
        l=mid
    else:
        r=mid