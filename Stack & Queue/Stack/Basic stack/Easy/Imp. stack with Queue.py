from collections import deque
class MyStack:
    def __init__(self):
        self.q=deque()
    def push(self,x):
        self.q.append(x)
    def pop(self):
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()
    def top(self):
        return self.q[-1]
    def empty(self):
        return len(self.q)==0

stack=MyStack()
stack.push(5)
stack.push(1)
stack.push(6)
stack.push(3)
stack.push(9)
stack.pop()


print(stack.q)
# print(stack.top())
# print(stack.empty())