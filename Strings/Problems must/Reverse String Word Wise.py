def Reverse_String_Word_Wise(s):
    w=s.split()
    w=w[::-1]
    return " ".join(w)
print(Reverse_String_Word_Wise("I love datascience"))
