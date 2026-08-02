points = [[10,16],[2,8],[1,6],[7,12],[11,17]]
def ballon(points):
    ans=len(points)
    points.sort()
    prev=points[0]
    for i in range(1,len(points)):
        curr=points[i]
        if prev[1]>=curr[0]:
            ans-=1
            prev=[curr[0],min(curr[1],prev[1])]
        else:
            prev=curr
    return ans
print(ballon(points))