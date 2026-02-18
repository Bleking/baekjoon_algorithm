# 백준 11057번 오르막 수 실버 1

import sys

N = int(sys.stdin.readline())

dp = [[0] * 10 for _ in range(N)]
for idx in range(10):
  dp[0][idx] = 1

for i in range(1, N):
  for j in range(10):
    for k in range(j, 10):
      dp[i][j] += (dp[i-1][k] % 10007)

print(sum(dp[N-1]) % 10007)
