def Longest_subarray_with_zero_sum(arr):
    sum=0
    hashmap={}
    for i in range(len(arr)):
        sum+=arr[i]
        if sum==0:
            max_length=i+1
        elif sum in hashmap:
            max_length=max(max_length,i-hashmap[sum])
        else :
            hashmap[sum]=i
    return max_length
print(Longest_subarray_with_zero_sum([1,-1,3,2,-2,-8,1,7,10,23]))

