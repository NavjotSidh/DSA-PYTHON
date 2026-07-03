def Fibonacci(n):
    if n==0:
        return 0
    if n==1:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

def print_fibonacci(n):
    for i in range(n):
        print(Fibonacci(i))
print_fibonacci(9)
