s="madam"
left=0
right=len(s)-1
while left < right :
    if s[left]!=s[right]:
        print('False')
        break
    left+=1
    right-=1
    print('true')
    break

