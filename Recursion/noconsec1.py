def Noconsec1(n,curr="",prev=0):
    if n==0:
        print(curr)
        return
    Noconsec1(n-1,curr+"0",prev=0)
    if prev==0:
        Noconsec1(n-1,curr+"1",prev=1)
Noconsec1(3)