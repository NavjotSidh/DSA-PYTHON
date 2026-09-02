s = "ADOBECODEBANC"
t = "ABC"
need={}
for i in t:
    need[i]=need.get(i,0)+1
left=0
have={}
have_count = 0
ans = ""
ans_len = float("inf")

for right in range(len(s)):
    ch=s[right]
    have[ch]=have.get(ch,0)+1
    if ch in need and have[ch]==need[ch]:
        have_count+=1
    while have_count==len(need):
        win_len=right-left+1
        if win_len<ans_len:
            ans_len=win_len
            ans=s[left:right+1]
        left_ch=s[left]
        have[left_ch]-=1
        if left_ch in need and have[left_ch]<need[left_ch]:
            have_count-=1
        left+=1
print(ans)