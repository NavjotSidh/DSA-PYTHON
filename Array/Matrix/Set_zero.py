def set_zero(matrix):
    m=len(matrix)
    n=len(matrix[0])

    row=set()
    col=set()
    #find zero
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row.add(i)
                col.add(j)

    for i in row:
        for j in range(n):
            matrix[i][j]=0

    for j in col:
        for i in range(m):
            matrix[i][j]=0
    return matrix
print(set_zero([[1,1,1],[1,0,1],[1,1,1]]))