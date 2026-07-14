def min_kadane(arr):
    min_sum=float('inf')
    curr_sum=0
    for i in arr:
        curr_sum=min(i,i+curr_sum)
        min_sum=min(min_sum,curr_sum)

    return min_sum
def max_kadane(arr):
    max_sum=float('-inf')
    curr_sum=0
    for i in arr:
        curr_sum=max(i,i+curr_sum)
        max_sum=max(curr_sum,max_sum)
    return max_sum

arr = [5, -3, 5]
max_sum=max_kadane(arr)
min_sum=min_kadane(arr)
total=sum(arr)
if total<0:
    print(max_sum)
else:
    print(total-min_sum)
