#Given a collection of intervals, merge all overlapping intervals.
intervals=[[1,3],[2,6],[8,10],[15,18]]
intervals.sort(key=lambda x:x[0])
merged=[]
for i in intervals:
    if not merged:
        merged.append(i)
    elif merged[-1][1] >= i[0]:
        merged[-1][1]=max(merged[-1][1],i[-1])
    else:
        merged.append(i)
print(merged)