arr = [1,7,3,6,5,6]
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=arr[i]+prefix[i-1]
# print(prefix)
total=prefix[-1]
l=0
r=0
for i in range(len(prefix)):
    if i==0:
        l=0
    else:
        l=prefix[i-1]
    r=total-prefix[i]
    if l==r:
        print(i)