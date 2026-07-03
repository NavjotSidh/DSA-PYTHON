import heapq
stones=[2,7,4,1,8,1]
def laststone(stones):
    heap=[]
    for i in stones:
        heapq.heappush(heap,-i)
    while len(heap)>1:
        a=-heapq.heappop(heap)
        b=-heapq.heappop(heap)
        diff=a-b
        if diff!=0:
            heapq.heappush(heap,-diff)
    if len(heap)==0:
        return 0
    else:
        return -heap[0]
print(laststone(stones))