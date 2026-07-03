def insertion_sort(arr):
    for i in range(0,len(arr)):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr
print(insertion_sort([3,5,6,4,8,9,10,7,1]))

