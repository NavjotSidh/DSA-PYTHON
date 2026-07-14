#how many subarray with sum k possible
arr=[1,-1,1,1,1,-1,1,1,1,1,-1]
k=3

curSum=0
res=0
prefixSum={0:1}
for n in arr:
    curSum+=n
    diff=curSum-k

    res+=prefixSum.get(diff,0)
    prefixSum[curSum]=1+prefixSum.get(curSum,0)
print(res)