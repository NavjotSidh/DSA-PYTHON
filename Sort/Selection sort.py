def Selection_sort(arr):
    for i in range(len(arr)):
        min=arr[i]
        indx=i
        for j in range(i+1,len(arr)):
            if arr[j]<min:
                min=arr[j]
                indx=j
            arr[i],arr[indx]=arr[indx],arr[i]
    return arr
print(Selection_sort([5,3,8,6,7,2]))
