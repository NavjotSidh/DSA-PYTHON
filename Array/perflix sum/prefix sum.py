arr = [3, -1, 0, 5, 3, -2, 5]

prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print("Prefix Sum Array:", prefix)

#Range Sum

l=2
r=5
if l ==0:
    range_sum=prefix[r]
else:
    range_sum = prefix[r]-prefix[l-1]
print('Range sum :',range_sum)