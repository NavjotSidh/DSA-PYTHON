n=19

def happy_num(n):
    seen=set()
    while n !=1 :
        if n in seen:
            return False
        total = 0
        seen.add(n)
        while n:
            digit=n%10
            total+=digit*digit
            n//=10
        n=total
    return True
print(happy_num(n))