height=[0,1,0,2,1,0,1,3,2,1,2,1]
n=len(height)
l,r=0,n-1
res=0
leftmax,rightmax=height[l],height[r]
while l<r:
    if leftmax<=rightmax:
        l+=1
        leftmax=max(leftmax,height[l])
        res+=leftmax-height[l]
    else:
        r-=1
        rightmax=max(rightmax,height[r])
        res+=rightmax-height[r]
print(res)