def paf(s,left,right):
    if left>=right:
        return True
    if s.lower()[left]!=s.lower()[right]:
        return False
    return paf(s,left+1,right-1)
s="Madam"
print(paf(s,0,len(s)-1))
