# 백준 1965번 	상자넣기 실버 2

import sys

n = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

dp = [1] * n
for i in range(n):
  for j in range(i):
    if boxes[i] > boxes[j]:
      dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))
