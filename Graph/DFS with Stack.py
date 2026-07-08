#using Stack
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
    def size(self):
        return len(self.st)
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

visited=[False]*n
st=Stack()
ans=[]

visited[0]=True
ans.append(0)
st.push(0)
while st.size()>0:
    top=st.pop()
    for i in adjList[top]:
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            st.push(i)
print(ans)