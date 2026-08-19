N=4
S="1101"
S = list(S)
Cash=5
A=1
B=2


if A<B:
    l = 0
    for r in range(len(S)):
        if S[r]=="0" and Cash>=A:
            S[r],S[l]=S[l],S[r]
            Cash-=A
            l+=1
for i in range(len(S)):
    if S[i]=="1" and Cash>=B:
        S[i]="0"
        Cash-=B
    elif S[i] == "1":
        break

print("".join(S))