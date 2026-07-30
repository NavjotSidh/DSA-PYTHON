bills = [5,5,5,10,20]
def lemonade(bills):
    five=0
    ten=0
    for i in bills:
        if i==5:
            five+=1
        if i==10:
            if not five:
                return False
            else:
                five-=1
                ten+=1
        if i==20:
            if not five:
                return False
            else:
                if ten>0 and five>0:
                    ten-=1
                    five-=1
                elif five>2:
                    five-=3
                else:
                    return False
    return True
print(lemonade(bills))