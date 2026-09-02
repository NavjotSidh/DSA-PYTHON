temperatures = [73,74,75,71,69,72,76,73]
stack=[]
ans=[0]*len(temperatures)
for i,num in enumerate(temperatures):
    while stack and stack[-1][1]<num:
        a,b=stack.pop()
        ans[a]=i-a
    stack.append((i,num))
print(ans)