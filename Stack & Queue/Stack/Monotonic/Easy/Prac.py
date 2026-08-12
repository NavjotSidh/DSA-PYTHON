heights = [2,1,5,6,2,3]
stack=[]
best=0

for i,h in enumerate(heights):
    start=i
    while stack and stack[-1][1]>h:
        indx,hgt=stack.pop()
        area=hgt*(i-indx)
        best=max(best,area)
        start=indx
    stack.append((i,h))
print(best)