ans = 0
n=101
for i in range(32):
    bit = n & 1
    ans = (ans << 1) | bit
    n >>= 1
print(ans)