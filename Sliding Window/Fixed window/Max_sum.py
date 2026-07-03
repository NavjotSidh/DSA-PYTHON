def Max_sum(arr,k):
    window_sum=sum(arr[:k])
    max_sum=window_sum

    for i in range(k,len(arr)):
        window_sum=window_sum+arr[i]-arr[i-k]
        max_sum=max(window_sum,max_sum)
    return max_sum
print(Max_sum([2, 1, 5, 1, 3, 2], 3))
