class Queue():
    def __init__(self):
        self.s1=[]
        self.s2=[]

    def push(self,x):
        self.s1.append(x)

    def pop(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        return self.s2[-1]

    def empty(self):
        return len(max(self.s1,self.s2))==0

q=Queue()
q.push(1)
q.push(1)
q.push(2)
q.push(3)
q.pop()
q.push(4)

print(q.s1)
print(q.s2)