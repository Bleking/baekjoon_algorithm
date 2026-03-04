# 백준 14501번 퇴사 실버 3

import sys

N = int(sys.stdin.readline())

time, price = [], []
for _ in range(N):
  T, P = map(int, sys.stdin.readline().split())
  time.append(T)
  price.append(P)

dp = [0] * (N+1)

for i in range(N):
  for j in range(i+time[i], N+1):
    if dp[i] + price[i] > dp[j]:
      dp[j] = dp[i] + price[i]

print(dp[N])
