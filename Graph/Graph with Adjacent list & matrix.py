edges=[(0,1),(0,3),(0,4),(1,2),(1,5),(2,4),(3,4)]
n=6   #Nodes
e=7   #Edges
adjList=[]
adjMatrix=[]
for i in range(n):
    adjList.append([])
    adjMatrix.append([0]*n)
# print(adjMatrix)

# for edge in edges:
#     x=edge[0]
#     y=edge[1]
#     adjList[x].append(y)
#     adjList[y].append(x)
# for i in range(n):
#     print(i,"-->",adjList[i])

for i in range(e):
    x=edges[i][0]
    y=edges[i][1] 

    adjMatrix[x][y]=1
    adjMatrix[y][x]=1
for i in adjMatrix:
    print(i)