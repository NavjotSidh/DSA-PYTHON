arr=[1, 2, 3, 7, 5]
target=12
cur_sum = 0
start = 0
for i in range(len(arr)):
    cur_sum += arr[i]
    while cur_sum>target and start <= i :
        cur_sum -= arr[start]
        start+=1

        if target == cur_sum:
            print(arr[start:i+1])
