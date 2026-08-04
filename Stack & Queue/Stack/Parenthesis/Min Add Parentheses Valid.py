s = "())"
def min_add(s):
    n=len(s)
    stack=[]
    for i in range(n-1,-1,-1):
        ch=s[i]
        if ch ==')':
            stack.append(ch)
        elif ch=='(':
            if stack and stack[-1]==')':
                stack.pop()
            else:
                stack.append(ch)
    return len(stack)
print(min_add(s))