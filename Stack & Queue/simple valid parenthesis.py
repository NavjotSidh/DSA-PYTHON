def Valid_parenthesis(s):
    stack=[]
    n=len(s)
    if n%2==1:
        return False
    for ch in s:
        if ch=='(' or ch=='{' or ch=='[':
            stack.append(ch)
        else:
            if len(stack)==0:
                return False
            top=stack.pop()
            if ch==')' and top!="(":
                return False
            elif ch=='}' and top!='{':
                return False
            elif ch==']' and top!='[':
                return False
    return len(stack)==0
print(Valid_parenthesis("()[]{}"))