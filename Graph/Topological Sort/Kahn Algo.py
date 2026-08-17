from collections import deque

V=6
E = {
    (0,1),
    (0,2),
    (1,3),
    (2,3),
    (3,4),
    (2,5)
}
cycle=False
ans=[]
indegree=[0]*V
adjList=[[]for i in range(V)]
for x,y in E:
    adjList[x].append(y)
    indegree[y]+=1
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
if len(ans)!=V:
    cycle=True
# print(ans)
print(cycle)