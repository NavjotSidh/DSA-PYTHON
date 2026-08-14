import heapq
nums = [1,1,1,2,2,3]
k = 2
freq={}
for i in nums:
    freq[i]=freq.get(i,0)+1
heap=[]
for i in freq:
    heapq.heappush(heap,(freq[i],i))
    if len(heap)>k:
        heapq.heappop(heap)
print(heap[0])