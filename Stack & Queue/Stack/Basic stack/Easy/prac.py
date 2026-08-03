# Valid Parentheses
s = "{[]}"
stack=[]
pairs={
    ')':'(',
    ']':'[',
    '}':'{'
}
for ch in s:
    if ch in ("(","[","{"):
        stack.append(ch)
    else:
        if not stack:
            print(False)
            break
        if stack[-1] != pairs[ch]:
            print(False)
            break
        stack.pop()
if len(stack)==0:
    print(True)
else:
    print(False)