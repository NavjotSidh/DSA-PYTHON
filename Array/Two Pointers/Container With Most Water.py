height = [1,8,6,2,5,4,8,3,7]
n=len(height)

l=0
r=n-1
area=0
while l<r:
    area=max(area,min(height[l],height[r]) * (r-l))
    if height[l]< height[r]:
        l+=1
    else:
        r-=1
print(area)