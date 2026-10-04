nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    comp=0-nums[i]
    l=i+1
    r=len(nums)-1
    while l<r:
        if nums[l]+nums[r]==comp:
            print([nums[i], nums[l], nums[r]])
            l += 1
            r -= 1
        elif nums[l]+nums[r]<comp:
            l+=1
        else:
            r-=1
