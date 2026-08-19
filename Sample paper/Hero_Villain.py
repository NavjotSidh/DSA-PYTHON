villains=[2,1,2,4,1,14,3,1,2,5,4]
H=13
N=5
def solve(villains,H,N):
    def Possible(start):
        hero=1
        curr_sum=0
        for i in range(start,len(villains)):
            if villains[i]>H:
                return False
            elif curr_sum+villains[i]<=H:
                curr_sum+=villains[i]
            elif curr_sum+villains[i]>H:
                hero+=1
                curr_sum=villains[i]
                if hero > N:
                    return False
        return True

    l=0
    r=len(villains)
    while l<=r:
        mid=(l+r)//2
        if Possible(mid):
            r=mid-1
        else:
            l=mid+1
    return l
print(solve(villains,H,N))