def Check_pelindrome(s):
    left,right=0,len(s)-1
    while left<right:
            if s[left].lower() != s[right].lower():
              return False
            left+=1
            right-=1
    return True
print(Check_pelindrome("Madam"))