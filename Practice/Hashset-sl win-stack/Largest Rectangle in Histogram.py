heights = [2, 1, 5, 6, 2, 3]
n=len(heights)
start=0
stack=[]
area=0
for i,num in enumerate(heights):
    start=i
    while stack and stack[-1][1]>num:
        a,b=stack.pop()
        width=i-a
        area=max(area,b*width)
        start=a
    stack.append((start,num))
for i,num in stack:
    area=max(area,num*(n-i))
print(area)