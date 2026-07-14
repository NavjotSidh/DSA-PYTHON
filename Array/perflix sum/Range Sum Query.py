arr=[2, 4, 1, 7, 3, 6]
Queries=[
(1,3),
(2,5),
(0,4),]
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=arr[i]+prefix[i-1]
print(prefix)

for query in Queries:
    a=query[0]
    b=query[1]
    if a==0:
        print(prefix[b])
    else:
        print(prefix[b]-prefix[a-1])
