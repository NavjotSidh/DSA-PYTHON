def Is_unique(s):
    seen=set()
    for ch in s:
        if ch in seen:
            return False
        seen.add(ch)
    return True
print(Is_unique("ban"))