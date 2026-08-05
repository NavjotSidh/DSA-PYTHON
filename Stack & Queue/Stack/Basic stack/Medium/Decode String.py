s="3[a]2[bc]"
def decode_string(s):
    stack=[]
    currstring=''
    currNum=0

    for i in s:
        if i.isdigit():
            currNum=currNum*10 + int(i)
        elif i=='[':
            stack.append((currstring,currNum))
            currstring=''
            currNum=0
        elif i==']':
            prevstring,num=stack.pop()
            currstring=prevstring+num*currstring
        else:
            currstring+=i
    return currstring
print(decode_string(s))