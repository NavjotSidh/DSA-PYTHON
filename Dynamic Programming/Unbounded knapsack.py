#Bounded / 1-0 Knapsack
value=[10,5,8,5,3]
weight=[3,2,4,6,4]
W=6
n=len(value)

def knapsack(i,W,n,value,weight):
    if i>=n:
        return 0
    take=0
    #Take
    if weight[i]<=W:
        take=value[i]+knapsack(i,W-weight[i],n,value,weight)

    no_take=0
    #not take
    no_take=knapsack(i+1,W,n,value,weight)
    return max(take,no_take)
ans=knapsack(0,W,n,value,weight)
print(ans)