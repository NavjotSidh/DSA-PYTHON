nums = [2, 7, 11, 15]
target = 9
seen={}
for i,num in enumerate(nums):
    comp=target-num
    if comp in seen:
        print([i,seen[comp]])
        break
    seen[num]=i
