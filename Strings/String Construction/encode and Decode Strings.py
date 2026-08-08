from tokenize import endpats

st=["neet", "coder"]

def encode(st):
    s=''
    for i in st:
        s+=str(len(i))+'#'+i
    return s

def decode(s):
    i=0
    ans=[]
    while i<len(s):
        j=i
        while s[j]!='#':
            j+=1
        length=int(s[i:j])
        word=s[j+1:j+1+length]
        ans.append(word)
        i=j+1+length
    return ans

print(st)
s=encode(st)
print(s)

print(decode(s))