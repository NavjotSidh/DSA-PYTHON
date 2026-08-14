import heapq
nums = [3,2,1,5,6,4]
k=2
n=len(nums)
heap=[]
for num in nums:
    heapq.heappush(heap,num)

    if len(heap)>k:
        heapq.heappop(heap)
print(heap[0])