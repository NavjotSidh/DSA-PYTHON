arr = [0,1,2,2,3,0,4]
val = 2
# l=0
# r=len(arr)-1
# while l<=r:
#     if arr[l]==val:
#         arr.pop(l)
#         r-=1
#     elif arr[r]==val:
#         arr.pop(r)
#         r-=1
#     else:
#         l+=1
#         r-=1
# print(len(arr))

write=0
for read in range(len(arr)):
    if arr[read]!=val:
        arr[write]=arr[read]
        write+=1
print(write)