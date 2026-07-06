arr=[2,0,2,1,1,0]
l=m=0
r=len(arr)-1
while m<=r:
    if arr[m]==0:
        arr[l],arr[m]=arr[m],arr[l]
        l+=1
        m+=1
    elif arr[m]==1:
        m+=1
    else:
        arr[m],arr[r]=arr[r],arr[m]
        r-=1
print(arr)