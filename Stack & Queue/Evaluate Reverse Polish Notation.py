tokens = [2, 1, "+", 3, "*"]
stack=[]
for t in tokens:
    if t in {"+","-","*","/"}:
        a=stack.pop()
        b=stack.pop()
        if t=="+":
            stack.append(a+b)
        elif t=="-":
            stack.append(a-b)
        elif t=="*":
            stack.append(a * b)
        elif t=="/":
            stack.append(a/b)
    else:
        stack.append(t)
print(stack)