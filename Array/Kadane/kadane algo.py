def kadane(arr):
    max_sum=arr[0]
    cur_sum=arr[0]
    for i in range(1,len(arr)):
        cur_sum=max(arr[i],cur_sum+arr[i])
        max_sum=max(max_sum,cur_sum)
    print('Max sum :',max_sum)
kadane([-2, 1, -3, 4, -1, 2, 1, -5, 4])
kadane([-8, -3, -6, -2, -5, -4])