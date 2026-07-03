def Average_sum(arr,k):
    n=len(arr)
    window_sum=0
    result=[]
    for i in range(n):
        window_sum+=arr[i]

        if i>=k-1:
            result.append(window_sum/k)
            window_sum-=arr[i-k+1]
    return result
print(Average_sum([1,3,2,6,-1,4,1,8,2,5,9],5))