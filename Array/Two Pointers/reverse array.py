arr=[2,5,7,3,-1,0,-4]
left=0
right=len(arr)-1
while left < right:
    arr[left],arr[right] = arr[right],arr[left]
    left+=1
    right-=1
print(arr)