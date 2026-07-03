arr=[4,0,1,4,65,0,6,0, 0, 3, 12]
i=0
for j in range(len(arr)):
    if arr[j] != 0:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
print(arr)