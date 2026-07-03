is_sorted=True
arr = [-3, -1, 0, 2, 3, 4, 5]
for i in range(len(arr)-1):
    if arr[i]>arr[i+1]:
        is_sorted=False
        break
print('Is Sorted',is_sorted)