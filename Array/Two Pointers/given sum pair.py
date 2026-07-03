arr=[1, 2, 4, 6, 8]
left=0
right=len(arr)-1
target=10
while left<right:
    s=arr[left]+arr[right]
    if s==target:
        print(arr[left],arr[right])
        break
    elif s>target:
        right-=1
    else:
        left+=1

