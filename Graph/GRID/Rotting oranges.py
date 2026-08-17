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
oranges = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 1]
]
q=Queue()
fresh=0
rows=len(oranges)
cols=len(oranges[0])

for i in range(rows):
    for j in range(cols):
        if oranges[i][j]==2:
            q.push((i,j))
        elif oranges[i][j]==1:
            fresh+=1
minutes=0
while q and fresh>0:
    for i in range(q.size()):
        cr,cc=q.pop()
        directions =
        for dr,dc in [(1, 0),(-1, 0),(0, 1),(0, -1) ]:
            nr=cr+dr
            nc=cc+dc
            if (0<=nr<rows and 0<=nc<cols and oranges[nr][nc]==1):
                oranges[nr][nc] = 2
                fresh-=1
                q.push((nr,nc))
    minutes+=1
if fresh>0:
    print("Not possible")
else:
    print(minutes)