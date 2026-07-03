def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid= len(arr)//2
    left_arr=arr[:mid]
    right_arr=arr[mid:]
    left_sorted=merge_sort(left_arr)
    right_sorted=merge_sort(right_arr)
    return merge(left_sorted,right_sorted)

def merge(left,right):
    i=j=0
    result=[]
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        elif right[j]<left[i]:
            result.append(right[j])
            j+=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
print(merge_sort([2,6,5,1,7,4,3]))

