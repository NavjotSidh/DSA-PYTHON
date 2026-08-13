text1 = "abcde"
text2 = "ace"

def rec(i,j,text1,text2):
    if i>=len(text1) or j>=len(text2):
        return 0
    if text1[i]==text2[j]:
        return 1+rec(i+1,j+1,text1,text2)

    one=rec(i+1,j,text1,text2)
    two=rec(i,j+1,text1,text2)
    return max(one,two)
print(rec(0,0,text1,text2))