tokens = ["2","1","+","3","*"]
stack=[]
for i in tokens:
    if i=="+":
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b)
    elif i=="-":
        a=stack.pop()
        b=stack.pop()
        stack.append(b-a)
    elif i=="*":
        a=stack.pop()
        b=stack.pop()
        stack.append(a*b)
    elif i=="/":
        a=stack.pop()
        b=stack.pop()
        stack.append(b//a)
    else:
        stack.append(int(i))
print(stack[-1])