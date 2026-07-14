arr = [10, 20, 30, 40, 50]
diffArray=[0]*len(arr)
diffArray[0]=arr[0]
for i in range(1,len(arr)):
    diffArray[i]=arr[i]-arr[i-1]
print(diffArray)