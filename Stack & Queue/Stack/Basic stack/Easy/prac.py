s=["4", "13", "5", "/", "+"]
stack=[]

for ch in s:
    if ch.isdigit():
        stack.append(int(ch))
    elif ch=='+':
        a=stack.pop()
        b=stack.pop()
        stack.append(a+b)
    elif ch=='-':
        a=stack.pop()
        b=stack.pop()
        stack.append(b-a)
    elif ch=='*':
        a=stack.pop()
        b=stack.pop()
        stack.append(a*b)
    elif ch=='/':
        a=stack.pop()
        b=stack.pop()
        stack.append(int(b)/int(a))
