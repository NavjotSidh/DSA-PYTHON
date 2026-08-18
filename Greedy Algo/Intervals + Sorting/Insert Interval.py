intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newinterval = [4,8]
def insert_interval(intervals,newinterval):
    ans=[]
    intervals.sort(key=lambda x:x[0])
    for i in range(len(intervals)):
        if newinterval[1]<intervals[i][0]:
            ans.append(newinterval)
            return ans+intervals[i:]
        elif newinterval[0]>intervals[i][1]:
            ans.append(intervals[i])
        else:
            newinterval=[min(newinterval[0],intervals[i][0]),max(newinterval[1],intervals[i][1])]
    ans.append(newinterval)
    return ans
print(insert_interval(intervals,newinterval))