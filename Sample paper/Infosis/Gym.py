A=[4,3,2,7,6]
E=20
N=5
def gym(A,E,N):
    ans=0
    A.sort(reverse=True)
    i = 0
    excr_count = 0
    while E>0:
        if i == N:
            return -1
        if excr_count<2:
            ans+=1
            E-=A[i]
            excr_count+=1
        else:
            excr_count=0
            i+=1

    return ans
print(gym(A,E,N))