def Is_valid(arr):
    stack=[]
    mapping={')':'(','}':'{',']':'['}
    for char in arr:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()
    return len(stack) == 0
print(Is_valid("({[})"))