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
edges=[(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]
n=6   #Nodes
e=7   #Edges
adjList=[]
for i in range(n):
    adjList.append([])
for edge in edges:
    x=edge[0]
    y=edge[1]
    adjList[x].append(y)
    adjList[y].append(x)


q=Queue()
visited=[False]*n
ans=[]

q.push(2)
visited[2]=True
ans.append(2)

while q.size()>0:
    front=q.pop()
    for i in adjList[front]:
        if not visited[i]:
            q.push(i)
            visited[i] = True
            ans.append(i)
print(ans)