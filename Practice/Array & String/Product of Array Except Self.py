nums = [1, 2, 3, 4]
prefix=[0]*len(nums)
prefix[0]=nums[0]

suffix=[0]*len(nums)
suffix[len(nums)-1]=nums[len(nums)-1]

for i in range(1, len(nums)):
    prefix[i] = nums[i] * prefix[i-1]

for i in range(len(nums)-2,-1,-1):
    suffix[i]=nums[i]*suffix[i+1]
ans=[]
for i in range(len(nums)):
    if i==0:
        ans.append(suffix[i + 1] *1)
    elif i==len(nums)-1:
        ans.append(1* prefix[i - 1])
    else:
        ans.append(suffix[i+1]*prefix[i-1])
print(ans)