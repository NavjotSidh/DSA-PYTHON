def Interaction(num1,num2):
    freq={}
    res=[]
    for i in num1:
        freq[i]=freq.get(i,0)+1
    for num in num2:
        if num in freq and freq[num]>0:
            res.append(num)
    return res
print(Interaction([1,2,2,1],[3,2]))