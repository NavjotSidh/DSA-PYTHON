N = 12345
s=str(N)
arr=list(s)
l=0
r=len(s)-1
while l<=r:
    arr[r]=arr[l]
    r-=1
    l+=1
print(int("".join(arr)))