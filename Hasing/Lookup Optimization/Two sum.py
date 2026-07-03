def Two_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        needed=target-num

        if needed in seen:
            return [needed,num]
        seen[num]=i
print(Two_sum([2,5,8,2,6,0,9],7))


