stack=[]
minStack=[]

def push(val):
    stack.append(val)
    if not minStack or minStack[-1]>=val:
        minStack.append(val)
    else:
        minStack.append(minStack[-1])
def pop():
    stack.pop()
    minStack.pop()
def top():
    return stack[-1]
def getmin():
    return minStack[-1]