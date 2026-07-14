def Max_sum_array(arr):
    max_sum = float('-inf')
    ans = []
    sum = 0

    start = 0
    end = 0
    temp_start = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum > max_sum:
            max_sum = sum
            start = temp_start
            end = i
        if sum < 0:
            sum = 0
            temp_start = i + 1
    return max_sum, "at", arr[start:end + 1]
print(Max_sum_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
