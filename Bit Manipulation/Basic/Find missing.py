nums = [3, 0, 1]

ans = len(nums)

for i, num in enumerate(nums):
    ans ^= i
    ans ^= num

print(ans)