# push(x)
# pop()
# top()
# getMin()
stack=[]
min_stack = [float('inf')]

def push(x):
    stack.append(x)
    if x<min_stack[-1]:
        min_stack.append(x)
def pop():
    x = stack.pop()
    if x == min_stack[-1]:
        min_stack.pop()
def top():
    return stack[-1]
def getMin():
    return min_stack[-1]

push(5)
push(3)
push(7)
push(2)
pop()
print(stack)
print(getMin())