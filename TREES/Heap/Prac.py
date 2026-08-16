import heapq
nums = [1,1,1,2,2,3]
k = 2
freq={}
for i in nums:
    freq[i]=freq.get(i,0)+1

# print(freq)
h=[]
for num,count in freq.items():
    heapq.heappush(h,(count,num))
    if len(h)>k:
        heapq.heappop(h)
ans=[num for count,num in h]
print(ans[0])