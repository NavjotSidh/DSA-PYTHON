result=[]
def backtrack(ind,total,bracket):
    if ind>=len(bracket):
        if total==0:
            result.append("".join(bracket))
        return
    if total>len(bracket)//2:
        return
    elif total<0:
        return
    bracket[ind]="("
    sum=total+1
    backtrack(ind+1,sum,bracket)
    bracket[ind]=")"
    sum=total-1
    backtrack(ind+1,sum,bracket)
backtrack(0,0,[])
print(result)