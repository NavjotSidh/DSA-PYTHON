nums = [2, 3, -2, 4]
curr_max = nums[0]
curr_min = nums[0]
best = nums[0]

for i in nums[1:]:
    old_max=curr_max
    old_min=curr_min

    curr_max=max(i,i*old_max,i*old_min)
    curr_min=min(i,old_min*i,old_max*i)
    best=max(best,curr_max)
print(best)