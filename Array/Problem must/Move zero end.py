def Move_zero_to_end(arr):
    left=0
    for right in range(len(arr)):
        if arr[right]!=0:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
    return arr
def Move_negative_to_end(arr):
    right=len(arr)-1
    left=0
    while left<=right:
        if arr[left]<0:
            arr[left],arr[right]=arr[right],arr[left]
            right-=1
        else:
            left+=1
    return arr
print(Move_negative_to_end([2,0,-3,-4,0,7,0,-8,9]))
