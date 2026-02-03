# 백준 2293번 동전 1 골드 4

import sys

n, k = map(int, sys.stdin.readline().split())

coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

dp = [0] * (k+1)
dp[0] = 1

for c in coins:
    for i in range(c, k+1):
        dp[i] += dp[i-c]

print(dp[k])
