#Find the maximum average of any contiguous subarray of size k
arr = [1, 12, -5, -6, 50, 3]
k = 4
window_avg=sum(arr[:k])/k
max_avg=window_avg
for right in range(k,len(arr)):
    window_avg+=arr[right]/k
    window_avg-=arr[right-k]/k
    max_avg=max(max_avg,window_avg)
print(max_avg)