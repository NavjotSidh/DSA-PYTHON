def solve():
    r,c=map(int,input().split())
    matrix=[]
    for _ in range(r):
        row=list(map(int,input().split()))
        matrix.append(row)
    print(matrix)
if __name__=="__main__":
    solve()