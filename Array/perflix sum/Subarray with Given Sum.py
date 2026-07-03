arr=[2,5,3,7,1,9,3]
prefix=[0]*len(arr)
prefix[0]=arr[0]
for i in range(1,len(arr)):
    prefix[i]=prefix[i-1]+arr[i]
print("prefix :",prefix)

target = 17
cur_sum=0
l=0
r=len(arr)
for i in range(len(arr)):
    cur_sum += arr[i]

    while cur_sum>target and l <= r:
        cur_sum -= arr[l]
        l+=1

        if cur_sum==target:
         print("subarray found from ",l,'to',r)
         print('Subarray :',arr[l:r+1])
         break
        else:
             print('not possible')

