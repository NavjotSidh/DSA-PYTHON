class Queue:
    def __init__(self):
        self.q=[]
        self.front=-1

    def push(self,x):
        if self.front==-1:
            self.front=0
        self.q.append(x)
    def pop(self):
        if len(self.q) == 0:
            return -1
        return self.q.pop(0)
    def getFront(self):
        if len(self.q)==0:
            return -1
        return self.q[self.front]
    def size(self):
        return len(self.q)-self.front
edges = [
    (0, 1),
    (0, 3),
    (0, 4),
    (4, 1),
    (4, 3),
    (3, 2)
]
q=Queue()
n=5
adjlist=[]
ans=[]
indegree=[0]*n
for i in range(n):
    adjlist.append([])
for a,b in edges:
    indegree[b]+=1
    adjlist[a].append(b)
for i in range(n):
    if indegree[i]==0:
        ans.append(i)
        q.push(i)
while q.size()>0:
    front=q.pop()
    for i in adjlist[front]:
        indegree[i]-=1
        if indegree[i]==0:
            ans.append(i)
            q.push(i)
print(len(ans)==n)