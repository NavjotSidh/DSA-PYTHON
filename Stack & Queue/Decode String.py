s="3[a2[c]]"
stack=[]
for i in s:
    if i != "]":
        stack.append(i)
    else:
        substr=""
        while stack[-1]!="[":
            substr=stack.pop()+substr
        stack.pop()
        k=""
        while stack and stack[-1].isdigit():
            k=stack.pop()+k
        stack.append(int(k)*substr)
print(stack)
