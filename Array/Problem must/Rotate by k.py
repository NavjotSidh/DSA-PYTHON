# def Rotate_by_k(arr,k):
#     n=len(arr)
#     k=k%n
#     return  arr[-k:] +arr[:-k]
# print(Rotate_by_k([2,4,-1,3,2,9],2))
# # space complexity = O(n)

def Rotate_by_k(arr,k):
    n=len(arr)
    k=k%n
    def Reverse(start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1
    Reverse(0,n-1)
    Reverse(0,k-1)
    Reverse(k,n-1)
    return arr
print(Rotate_by_k([2,4,-1,3,2,9],2))
