# 백준 9465번 스티커 실버 1

import sys

T = int(sys.stdin.readline())

for t in range(T):
  n = int(sys.stdin.readline())

  stickers = []
  for _ in range(2):
    stickers.append(list(map(int, sys.stdin.readline().split())))

  dp = [[0] * n for _ in range(3)]
  dp[1][0], dp[2][0] = stickers[0][0], stickers[1][0]

  for i in range(1, n):
    dp[0][i] = max(dp[1][i-1], dp[2][i-1])
    dp[1][i] = stickers[0][i] + max(dp[0][i-1], dp[2][i-1])
    dp[2][i] = stickers[1][i] + max(dp[0][i-1], dp[1][i-1])

  print(max(dp[0][n-1], dp[1][n-1], dp[2][n-1]))
