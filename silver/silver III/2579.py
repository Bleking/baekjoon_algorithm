# 백준 1260번 계단 오르기 실버 3

import sys

n = int(sys.stdin.readline())
stair = []
for _ in range(n):
  stair.append(int(sys.stdin.readline()))

dp = [0] * n
dp[0] = stair[0]

if n > 1:
  dp[1] = stair[0] + stair[1]
if n > 2:
  dp[2] = max(stair[0] + stair[2], stair[1] + stair[2])

for i in range(3, n):
  dp[i] = max(dp[i-3] + stair[i-1] + stair[i], dp[i-2] + stair[i])

print(dp[n-1])
