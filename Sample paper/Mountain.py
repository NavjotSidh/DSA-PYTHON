arr=[1,2,3,4,4,5]
l=len(arr)
count=0
if l%2!=0:
    m = l // 2
    for i in range(m-1,-1,-1):
        if arr[i]!=arr[i+1]-1:
            count+=1
            arr[i]=arr[i+1]-1
    j=m-1
    for i in range(m+1,l):
        if arr[i]!=arr[j]:
            count+=1
            arr[i]=arr[j]
        j-=1
else:
    m2=l//2
    m1=m2-1
    if arr[m1]==arr[m2]:
        for i in range(m1 - 1, -1, -1):
            if arr[i] != arr[i + 1] - 1:
                count += 1
                arr[i] = arr[i + 1] - 1
    else :
        arr[m1]=arr[m2]
        count+=1
        for i in range(m1 - 1, -1, -1):
            if arr[i] != arr[i + 1] - 1:
                count += 1
                arr[i] = arr[i + 1] - 1

    j = m1 - 1
    for i in range(m2 + 1, l):
        if arr[i] != arr[j]:
            count += 1
            arr[i] = arr[j]
        j-=1


print(arr)
print(count)