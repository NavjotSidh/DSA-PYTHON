nums=[2,3,1,1,4]
def jump_game(nums):
    mxreach=0
    for i in range(len(nums)):
        if i>mxreach:
            return False
        mxreach=max(mxreach,i+nums[i])
    return True
print(jump_game(nums))