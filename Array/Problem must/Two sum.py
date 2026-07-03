def Two_sum_hashing(arr,t):
    seen={}
    for i,n in enumerate(arr):
        compliment=t-n
        if compliment in seen:
            return (seen[compliment],i)
        seen[n]=i
# print(Two_sum_hashing([4,2,3,6,5,0,7],10))

def Two_sum_pointer(arr,t):
    arr.sort()
    left=0
    right=len(arr)-1
    while left<right:
        add=arr[left]+arr[right]
        if add == t:
            return (arr[left],arr[right])
        elif add<t:
            left+=1
        else:
            right-=1
    return False
print(Two_sum_pointer([4,2,3,6,5,0,7],10))