s="lee(t(c)o)de)"
def min_remove(s):
    s=list(s)
    stack=[]
    for i,ch in enumerate(s):
        if ch=='(':
            stack.append(i)
        elif ch==')':
            if stack:
                stack.pop()
            else:
                s[i]=''

    while stack:
        s[stack.pop()]=''
    return ''.join(s)
print(min_remove(s))