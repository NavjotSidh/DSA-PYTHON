import heapq
nums=[2,5,7,4,9,66,8,12]
def findkth(nums,k):
    h=[]
    for i in nums:
        heapq.heappush(h,i)
        if len(h)>k:
            heapq.heappop(h)
    return h[0]
print(findkth(nums,4))