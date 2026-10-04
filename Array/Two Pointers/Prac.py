from collections import Counter
# arr = [2, 4, 5, 9, 10]
# target = 13
# l=0
# r=len(arr)-1
# ans=[-1,-1]
# while l<r:
#     if arr[l]+arr[r]==target:
#         ans=[l,r]
#         break
#     elif arr[l]+arr[r]<target:
#         l+=1
#     else:
#         r-=1
# print(ans)
#
# nums = [-1, 0, 1, 2, -1, -4]
# target=0
# ans=[-1,-1,-1]
# nums.sort()
# for a in range(len(nums)-2):
#     l=a+1
#     r=len(nums)-1
#     comp=target-nums[a]
#     if nums[l]+nums[r]==comp:
#         ans=[nums[a],nums[l],nums[r]]
#     elif nums[l]+nums[r]<comp:
#         l+=1
#     else:
#         r-=1
# print(ans)

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# l=0
# r=len(height)-1
# area=0
# while l<r:
#     area=max(area,min(height[l],height[r])*(r-l))
#     if height[l]<height[r]:
#         l+=1
#     else:
#         r-=1
# print(area)

# nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
# n=set(nums)
# print(n)

# s = "abcabcbb"
# l=0
# ans=0
# seen=[]
# for r in range(len(s)):
#     while s[r] in seen:
#         seen.remove(s[r])
#         l+=1
#     seen.append(s[r])
#     ans=max(ans,(r-l)+1)
# print(ans)

# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# l=0
# curr=sum(arr[:3])
# best=sum(arr[:3])
# for i in arr[3:]:
#     curr=curr-arr[l]+i
#     best=max(best,curr)
#     l+=1
# print(best)

target = 7
nums = [2, 3, 1, 2, 4, 3]
n=len(nums)
l=0
ans=0
res=n
for r in range(n):
    ans += nums[r]
    while ans>=target:
        res = min(res, r - l + 1)
        ans-=nums[l]
        l+=1

print(res)