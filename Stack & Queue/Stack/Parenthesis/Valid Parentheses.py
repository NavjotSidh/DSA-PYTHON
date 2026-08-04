s="([)]"
def valid(s):
    stack=[]
    map={')':'(',']':'[','}':'{'}
    for i in s:
        if i in map.values():
            stack.append(i)
        elif i in map:
            if not stack or map[i]!=stack[-1]:
                return False
            stack.pop()
    return len(stack)==0
print(valid(s))