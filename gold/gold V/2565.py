# 백준 2565번 전깃줄 골드 5

import sys

N = int(sys.stdin.readline())
wires = []
for _ in range(N):
  a, b = map(int, sys.stdin.readline().split())
  wires.append((a, b))

wires.sort()

dp = [1] * N

for i in range(N):
  for j in range(i):
    if wires[i][1] > wires[j][1]:
      dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))
