def search_matrix(matrix,target):
    ROW,COL=len(matrix),len(matrix[0])
    top,bot=0,ROW-1
    while top<=bot:
        mid_row=(top+bot)//2
        if target<matrix[mid_row][0]:
            bot=mid_row-1
        elif target > matrix[mid_row][-1]:
            top=mid_row+1
        else:
            break
    if not(top<=bot):
        return False
    l,r=0,COL-1
    while l<=r:
        m=(l+r)//2
        if target<matrix[mid_row][m]:
            r=m-1
        elif target>matrix[mid_row][m]:
            l=m+1
        else:
            return True,[mid_row,m]
    if not(l<=r):
        return False
print(search_matrix([
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
],30))