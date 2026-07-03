def Bubble_sort(arr):
    n=len(arr)
    for i in range(n):
        isSwap=False
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
                isSwap=True
        if not isSwap:
            break
    return arr
print(Bubble_sort([5,3,8,4,6,7,2]))