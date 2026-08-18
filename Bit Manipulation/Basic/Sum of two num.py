a=5
b=3
while b!=0:
    carry=(a&b)<<1
    a=a^b
    b=carry
print(a)