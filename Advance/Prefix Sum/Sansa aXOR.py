def sansaXOR(arr):
    n=len(arr)
    res=0
    for i in range(n):
        count=(i+1)*(n-i)
        if count%2==1:
            res^=arr[i]
    return res
print(sansaXOR([3,4,5]))