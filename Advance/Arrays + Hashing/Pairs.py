def pairs(k, arr):
    # Write your code here
    freq={}
    res=0
    for i in arr:
        freq[i]=freq.get(i,0)+1
    for i in arr:
        res+= freq.get(i+k,0)
    return res
print(pairs(1,[1,1,2,2,3,4]))