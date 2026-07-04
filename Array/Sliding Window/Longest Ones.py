#Find the longest sequence of consecutive 1s.
# count=0
# maxi=0
# for i in arr:
#     if i==1:
#         count+=1
#         maxi=max(maxi,count)
#     else:
#         count=0
# print(maxi)

# Find the longest consecutive 1s after flipping at most 2 zeros.
arr = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
max_length=0
left=0
zero_count=0
for right in range(len(arr)):
    if arr[right] == 0:
        zero_count+=1
    while zero_count>k:
        if arr[left]==0:
            zero_count-=1
        left+=1
    max_length=max(max_length,right-left+1)
print(max_length)