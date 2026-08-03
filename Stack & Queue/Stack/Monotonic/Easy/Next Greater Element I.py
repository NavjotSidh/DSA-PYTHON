nums1=[3,1,2]
nums2=[1,3,4,2]
stack=[]
map={}

for i in nums2:
    while stack and stack[-1]<i:
        map[stack.pop()]=i
    stack.append(i)

while stack:
    map[stack.pop()]=-1

ans=[]
for i in nums1:
    ans.append(map[i])

print(ans)