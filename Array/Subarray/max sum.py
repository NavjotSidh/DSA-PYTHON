max_sum=float('-inf')
arr = [-2,1,-3,4,-1,2,1,-5,4]
for i in range(len(arr)):
    cur_sum=0
    for j in range(i,len(arr)):
        cur_sum += arr[j]
        max_sum= max(cur_sum,max_sum)
print(max_sum)