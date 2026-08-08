nums=[1,1,2,2,3,4,5,36,36,6,7,7,9,11,56]
i=0
for j in range(len(nums)):
    if nums[i]!=nums[j]:
        i+=1
        nums[i] = nums[j]
print(i+1)
print(nums[:i+1])