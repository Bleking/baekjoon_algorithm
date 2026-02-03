# 백준 2294번 동전 2 골드 5 

import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [100001] * (k+1)
dp[0] = 0

for c in coins:
    for i in range(c, k+1):
        dp[i] = min(dp[i], dp[i - c] + 1)

if dp[k] == 100001:
    print(-1)
else:
    print(dp[k])
