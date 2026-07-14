import copy
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

class Stack:
    def __init__(self):
        self.st = []

    def push(self, x):
        self.st.append(x)

    def pop(self):
        if len(self.st) == 0:
            return -1
        x = self.st[-1]
        self.st.pop()
        return x

    def top(self):
        if len(self.st) == 0:
            return -1
        return self.st[-1]
    def size(self):
        return len(self.st)

edges=[(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]
adjList3 = [
    [1],        # 0
    [0,5],      # 1
    [3,4,6],    # 2
    [2,4],      # 3
    [2,3],      # 4
    [1],        # 5
    [2],        # 6
    []          # 7
]

n=len(edges)-1
adjList=[]
adjMatrix=[]
for i in range(n):
    adjList.append([])
    adjMatrix.append([0]*n)
for edge in edges:
    x=edge[0]
    y=edge[1]

    adjList[x].append(y)
    adjList[y].append(x)

    adjMatrix[x][y]=1
    adjMatrix[y][x]=1
# print(adjMatrix)
# for i in range(n):
#     print(i,"-->",adjList[i])

visited=[False]*n
q=Queue()
ans=[]
def bfs(adjList,a):
    visited[a]=True
    q.push(a)
    ans.append(a)

    while q.size()>0:
        front=q.pop()
        for i in adjList[front]:
            if not visited[i]:
                visited[i]=True
                q.push(i)
                ans.append(i)
    return ans
# print(bfs(adjList,0))

# dfs with Stack
st=Stack()
def dfs(adjList,a):

    st.push(a)

    while st.size()>0:
        front=st.pop()
        if visited[front]:
            continue
        visited[front] = True
        ans.append(front)

        for i in reversed(adjList[front]):
            if not visited[i]:
                st.push(i)
    return ans
# print(dfs(adjList,0))

# dfs with recursion
def Dfs(i,adjlist,visited):
    visited[i]=True
    ans.append(i)
    for x in adjlist[i]:
        if not visited[x]:
            Dfs(x,adjlist,visited)
    return ans
# print(Dfs(0,adjList,visited))

#detect cycle with BFS
parent=[-1]*n
def Detect_cycle(i,parent,adjlist,visited):
    visited[i]=True
    q.push(i)
    while q.size() > 0:
        front=q.pop()
        for a in adjlist[front]:
            if not visited[a]:
                q.push(a)
                visited[a] = True
                parent[a] = front
            elif parent[front]!=a :
                return True

    return False
# print(Detect_cycle(0,parent,adjList,visited))

#detect cycle using dfs recursion
adjList2 = [
    [1],      # 0
    [0, 2],   # 1
    [1, 3],   # 2
    [2]       # 3
]
def detect(i,parent,adjlist,visited):
    visited[i]=True
    for x in adjlist[i]:
        if visited[x]:
            if parent[i]!=x:
                return True
        else:
            parent[x]=i
            if detect(x,parent,adjlist,visited):
                return True
    return False
# print(detect(0,parent,adjList2,visited))

def count(adjlist,visited,c):
    for a in range(n):
        if not visited[a]:
            Dfs(a,adjlist,visited)
            c+=1
    return c
# print(count(adjList,visited,0))

#NO of island
def Solve(r,c,adjmatrix):
    if r<0 or r>=len(adjmatrix) or c<0 or c>=len(adjmatrix[0]) or adjmatrix[r][c]==0:
        return
    adjmatrix[r][c]=0
    Solve(r+1,c,adjmatrix)
    Solve(r-1,c,adjmatrix)
    Solve(r,c+1,adjmatrix)
    Solve(r,c-1,adjmatrix)
def no_of_island(adjmatrix):
    ginti = 0
    for a in range(len(adjmatrix)):
        for b in range(len(adjmatrix[0])):
            if adjmatrix[a][b]==1:
                ginti+=1
                Solve(a,b,adjmatrix)
    return ginti
print(no_of_island(copy.deepcopy(adjMatrix)))


