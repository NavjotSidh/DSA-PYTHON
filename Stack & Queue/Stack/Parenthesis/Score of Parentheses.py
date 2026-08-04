s='(()(()))'
def score(s):
    stack=[0]
    for i in s:
        if i=='(':
            stack.append(0)
        else:
            curr=stack.pop()
            stack[-1]+=max(2*curr,1)
    return stack[-1]
print(score(s))