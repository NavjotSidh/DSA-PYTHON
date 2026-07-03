def equilibrium(arr):
    left_sum=0
    total_sum=sum(arr)
    for i in range(0,len(arr)):
        right_sum=total_sum-left_sum-arr[i]
        if right_sum==left_sum:
            return arr[i]
        left_sum+=arr[i]
print(equilibrium([1,3,5,2,2]))