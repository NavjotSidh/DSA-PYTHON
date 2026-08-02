intervals=[[1,3],[2,6],[8,10],[15,18]]
def merge_interval(intervals):
    intervals.sort()
    ans=[]
    ans.append(intervals[0])
    for i in intervals[1:]:
        if ans[-1][1]>=i[0]:
            ans[-1][1]=max(ans[-1][1],i[1])
        else:
            ans.append(i)
    return ans
print(merge_interval(intervals))