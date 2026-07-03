arr = [3, -1, 0, 3, 5]
def all_sub_array():
    for i in range(len(arr)):
        for j in range(i,len(arr)):
            print(arr[i:j+1])

def count_subarray():
    n=len(arr)
    print(n*(n+1)//2)
all_sub_array()
count_subarray()