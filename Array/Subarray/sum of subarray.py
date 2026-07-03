arr=[2,4,99,7,45,78,15,6,1]
total_sum=0
for i in range(len(arr)):
    cur_sum=0
    for j in range(i,len(arr)):
        cur_sum += arr[j]
        total_sum+=cur_sum
print('Sum is :',total_sum)