s="3[a]2[bc]"
def decode(s):
    stack=[]
    currString=''
    currNum=0

    for i,ch in enumerate(s):
        if ch.isdigit():
            currNum=currNum*10 + int(ch)
        elif ch=='[':
            stack.append((currString,currNum))
            currString=''
            currNum=0
        elif ch==']':
            prevstring,num=stack.pop()
            currString = prevstring + currString*num
        else:
            currString+=ch
    return currString
print(decode(s))