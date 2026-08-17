from collections import deque
numCourses = 4
prerequisites = [
    [1, 0],
    [2, 1],
    [3, 2]
]

cycle=False
ans=[]
indegree=[0]*numCourses
adjList=[[]for i in range(numCourses)]
for x,y in prerequisites:
    adjList[y].append(x)
    indegree[x]+=1
q=deque()
for i,val in enumerate(indegree):
    if val==0:
        q.append(i)
while q:
    curr_node=q.popleft()
    ans.append(curr_node)
    for i in adjList[curr_node]:
        indegree[i]-=1
        if indegree[i]==0:
            q.append(i)
if len(ans)==numCourses:
    print(ans)
else:
    print([])