arr=[1,-1,1,1,1,1]
def subarary_sum(arr,k):
    freq={0:1}
    res=0
    currSum=0

    for i in arr:
        currSum+=i
        diff=currSum-k
        res+=freq.get(diff,0)
        freq[currSum]=1+freq.get(currSum,0)
    return res
print(subarary_sum(arr,3))