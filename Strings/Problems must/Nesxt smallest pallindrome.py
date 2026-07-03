def next_smallest_palindrome(num):
    s = list(str(num))
    left=0
    n=len(s)
    right=n-1
    while left<right:
        s[right]=s[left]
        left+=1
        right-=1
        pal=int("".join(s))
        if pal>num:
            return pal
        carry=1

# print(next_smallest_palindrome(1327))
