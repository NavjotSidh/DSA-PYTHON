#using Stack
edges=[(0,1),(0,2),(1,3),(1,4),(2,5),(4,5)]
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
st=[0]
ans=[]


while len(st)>0:
    top=st.pop()
    if visited[top]:continue
    visited[top]=True
    ans.append(top)
    for i in adjList[top]:
        if not visited[i]:
            st.append(i)
print(ans)