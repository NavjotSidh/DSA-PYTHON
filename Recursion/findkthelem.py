def findkth(arr,k):
    if k==1:
        return arr[0]
    return findkth(arr[1:],k-1)