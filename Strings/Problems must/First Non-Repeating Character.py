def First_NonRepeating_Character(s):
    seen={}
    for ch in s:
        seen[ch]=seen.get(ch,0)+1

        if seen[ch] == 1:
            return ch
print(First_NonRepeating_Character("leetcode"))
