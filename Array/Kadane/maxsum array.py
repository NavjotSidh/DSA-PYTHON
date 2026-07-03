def Max_sum_array(arr):
    cur_sum=arr[0]
    max_sum=arr[0]
    start=0
    ans_start=0
    ans_end=0
    for i in range(1,len(arr)):
        if arr[i]>cur_sum+arr[i]:
            cur_sum=arr[i]
            start = i
        else:
            cur_sum+=arr[i]

        if cur_sum>max_sum:
            max_sum=cur_sum
            ans_start=start
            ans_end=i

    return max_sum,arr[ans_start:ans_end+1]
print(Max_sum_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
