nums=[-1,0,1,2,-1,-4]
def three_sum(nums):
    n=len(nums)
    nums.sort()
    ans=[]
    for i , a in enumerate(nums):
        if i>0 and nums[i]==nums[i-1]:
            continue
        l=i+1
        r=n-1
        while l<r:
            threesum = a + nums[l] + nums[r]
            if threesum>0:
                r-=1
            elif threesum<0:
                l+=1
            else:
                ans.append([a,nums[l],nums[r]])
                l+=1
                while l<r and nums[l]==nums[l-1]:
                    l+=1
    return ans
print(three_sum(nums))