def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr.pop()
    lower_arr=[]
    greater_arr=[]
    for i in arr:
        if i<pivot:
           lower_arr.append(i)
        else:
            greater_arr.append(i)
    return quick_sort(lower_arr) + [pivot] + quick_sort(greater_arr)
print(quick_sort([0,9,3,8,2,7,5]))