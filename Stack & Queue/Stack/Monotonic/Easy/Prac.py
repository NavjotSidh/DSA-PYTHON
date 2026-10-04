temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
n=len(temperatures)
stack=[]
ans=[0]*n
for i,temp in enumerate(temperatures):
    while stack and stack[-1][1]<temp:
        indx,Temp=stack.pop()
        ans[indx]=i-indx
    stack.append((i,temp))
print(ans)