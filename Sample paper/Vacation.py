N=10
M=5
K=2
arr=[6,9,3,2,7]
arr.sort()
x=[0]
for i in arr:
    x.append(i)
x.append(N+1)

l=1
r=l+K-1
ans=(x[r+1]-x[l-1])-1
for r in range(K+1,len(x)-1):
    l+=1
    ans=max(ans,x[r+1]-x[l-1]-1)
print(ans)