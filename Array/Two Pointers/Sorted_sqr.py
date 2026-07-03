arr = [-4, -1, 0, 3, 10]
ans=[0]*len(arr)
l=0
r=len(arr)-1
a=len(arr)-1
while l<=r:
    if abs(arr[l])>abs(arr[r]):
        ans[a]=arr[l]*arr[l]
        a-=1
        l+=1
    else:
        ans[a]=arr[r]*arr[r]
        a-=1
        r-=1
print(ans)