target = [2,3,4]
curr=1
ans=[]
i=0
while i <= len(target)-1:
    if curr<target[i]:
        ans.append("Push")
        ans.append("Pop")
        curr+=1
    else:
        ans.append("Push")
        i+=1
        curr+=1
print(ans)