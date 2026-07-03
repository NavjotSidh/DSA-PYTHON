def Reverse_string(s):
    return s[::-1]
# print(Reverse_string("call"))

def Check_paledrome(s):
    return s == s[::-1]
# print(Check_paledrome("call"))

def Extract_domain(email):
    start=email.index('@')
    return email[start+1:]
# print(Extract_domain('Sidhunavjot2007@gmail.com'))

def Remove_first_lsst(s):
    return s[1:-1]
# print(Remove_first_lsst("python"))