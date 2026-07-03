nums=[2,1,5,6,2,3]
n=len(nums)
stack=[] #pair:(index,height)
Maxarea=0
for i,h in enumerate(nums):
     start=i
     while stack and stack[-1][1]>h:
         index,height=stack.pop()
         Maxarea=max(Maxarea,height*(i-index))
         start=index
     stack.append([start,h])
for i,h in stack:
    Maxarea=max(Maxarea,h*(n-i))
print(Maxarea)
