n=16
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i & (i - 1)] + 1

print(dp)