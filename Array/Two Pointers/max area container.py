arr=[1,8,6,2,5,4,8,3,7,5,6,6]
left,right=0,len(arr)-1
max_area=0
while left<right:
    width=right-left
    area=min(arr[left],arr[right])*width
    max_area=max(area,max_area)
    if arr[left]<arr[right]:
        left+=1
    else:
        right-=1
print(max_area)