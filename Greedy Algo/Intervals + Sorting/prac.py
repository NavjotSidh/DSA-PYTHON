Intervals=[[1,2] ,[3,5], [6,7], [8,10], [12,16]]
new=[4,8]

res=[]
for indx,i in enumerate(Intervals):
    if i[0]>new[1]:
        res.append(new)
        res.extend(Intervals[indx:])
        break
    elif i[1]<new[0]:
        res.append(i)
    else:
        new=[min(i[0],new[0]),max(i[1],new[1])]
print(res)