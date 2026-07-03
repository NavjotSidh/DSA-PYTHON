arr = [3, -1, 0, 5, 3, -2, 5]
left=0
right=len(arr)-1

while left<right:
     arr[left] ,arr[right]=arr[right], arr[left]
     left +=1
     right -= 1
print('Traversed Array :',arr)
