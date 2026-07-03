class Stack:
    def __init__(self):
        self.st=[]

    def push(self,x):
        self.st.append(x)
    def pop(self):
        if len(self.st)==0:
            return -1
        x=self.st[-1]
        self.st.pop()
        return x
    def top(self):
        if len(self.st)==0:
            return -1
        return self.st[-1]


stack=Stack()
stack.push(5)
stack.push(8)
stack.push(3)
stack.push(1)
stack.pop()
print(stack.st)