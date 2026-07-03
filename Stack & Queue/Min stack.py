class Min_stack:
    def __init__(self):
        self.stack=[]
        self.minstack=[]

    def push(self,val:int):
        self.stack.append(val)
        if not self.minstack:
            self.minstack.append(val)
        else:
            self.minstack.append(min(self.minstack[-1],val))

    def pop(self):
        self.stack.pop()
        self.minstack.pop()

    def min(self):
        return self.minstack[-1]

    def top(self):
        return self.stack[-1]
m1=Min_stack()
m1.push(-2)
m1.push(-3)
m1.push(3)
print(m1.min())
print(m1.top())