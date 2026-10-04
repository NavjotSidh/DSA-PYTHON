intervals = [[1,3], [2,6], [8,10], [15,18]]
intervals.sort(key=lambda x:x[0])
ans=[intervals[0]]
for interval in intervals[1:]:
    if interval[0]<ans[-1][1]:
        ans[-1][1]=max(ans[-1][1],interval[1])
    else:
        ans.append(interval)
print(ans)