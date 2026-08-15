image = [
    [1, 1, 1],
    [0, 1, 0],
    [1, 0, 1]
]
sr = 1
sc = 1
color = 2
row=len(image)
col=len(image[0])
original = image[sr][sc]

def dfs(r,c,color):
    if r<0 or r>=row or c<0 or c>=col or image[r][c]!=original:
        return
    image[r][c]=color
    dfs(r+1,c,color)
    dfs(r,c+1,color)
    dfs(r-1,c,color)
    dfs(r,c-1,color)
    return image
print(dfs(sr,sc,color))