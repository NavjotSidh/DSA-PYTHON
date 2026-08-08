height =[0,1,0,2,1,0,1,3,2,1,2,1]

def RaonWtrTrp(height):
    n=len(height)
    water=0
    l=0
    r=n-1
    leftmax,rightmax=height[l],height[r]
    while l<r:
        if leftmax<=rightmax:
            l+=1
            leftmax=max(leftmax,height[l])
            water+=leftmax-height[l]
        else:
            r-=1
            rightmax=max(rightmax,height[r])
            water+=rightmax-height[r]
    return water
print(RaonWtrTrp(height))