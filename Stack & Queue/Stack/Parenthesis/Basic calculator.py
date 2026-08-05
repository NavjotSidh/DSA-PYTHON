s="(1+(4+5+2)-3)+(6+8)"
def basic_calculator(s):
    result=0
    sign=1
    stack=[]
    currNumber=0

    for ch in s:
        if ch.isdigit():
            currNumber=currNumber*10 + int(ch)
        elif ch=='+':
            result+=sign*currNumber
            currNumber=0
            sign=1
        elif ch=='-':
            result+=sign*currNumber
            currNumber=0
            sign=-1
        elif ch=='(':
            stack.append(result)
            stack.append(sign)
            result=0
            sign=1
            currNumber=0
        elif ch==')':
            result+=sign*currNumber
            currNumber=0

            result*=stack.pop()
            result+=stack.pop()
    result+=sign*currNumber
    return result
print(basic_calculator(s))