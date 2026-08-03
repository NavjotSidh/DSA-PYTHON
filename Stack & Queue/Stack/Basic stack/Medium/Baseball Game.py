ops = ["5","2","C","D","+"]
stack=[]
for i in ops:
    if i=="C":
        if stack:
            stack.pop()
    elif i=="+":
        if stack:
            stack.append((stack[-1])+stack[-2])

    elif i=="D":
        if stack:
            stack.append(stack[-1]*2)

    else:
        stack.append(int(i))
print(sum(stack))