costs = [[10,20],[30,200],[400,50],[30,20]]
# n=len(costs)
# diff=[]
# a=0
# for i in range(len(costs)):
#     a+=costs[i][0]
#     diff.append(costs[i][1]-costs[i][0])
# diff.sort()
# ans=a + sum(diff[:(n//2)])
# print(ans)

def twoCitySchedCost(costs):
    costs.sort(key=lambda x:x[1]-x[0])
    n=len(costs)//2
    ans=0

    for i in range(n):
        ans+=costs[i][1]
    for i in range(n,len(costs)):
        ans+=costs[i][0]
    return ans
print(twoCitySchedCost(costs))