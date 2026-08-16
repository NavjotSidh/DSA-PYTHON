import heapq
points = [[1,3],[-2,2],[5,8],[0,1]]
k = 2
h=[]
for x,y in points:
    dist=x*x + y*y
    heapq.heappush(h,(-dist,x,y))
    if len(h)>k:
        heapq.heappop(h)
ans=[[x,y]for dist,x,y in h]
print(ans)