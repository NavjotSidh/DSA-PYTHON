def sorted_remove_duplicates(arr):
    i=0
    for j in range(1,len(arr)):
        if arr[i]!=arr[j]:
            i+=1
            arr[i]=arr[j]
    return arr[:i+1]

# print(sorted_remove_duplicates([1,1,2,2,3,4,4,5,5,6]))

def Unsorted_remove_duplicates(arr):
    seen=set()
    result=[]
    for i in arr:
        if i not in seen:
            seen.add(i)
            result.append(i)
    return result
print(Unsorted_remove_duplicates([13,1,2,1,4,3]))
print(Unsorted_remove_duplicates([1,1,2,2,3,4,4,5,5,6]))

