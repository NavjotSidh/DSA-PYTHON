#Find the smallest subarray whose sum is at least 7.
arr = [2, 3, 1, 2, 4, 3]
target = 7
left=0
min_lenght= float('inf')
add=0
for right in range(len(arr)):
    add += arr[right]
    while add>=target:
        min_lenght=min(min_lenght,right-left+1)
        add-=arr[left]
        left+=1
print(min_lenght)