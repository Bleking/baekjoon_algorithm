# 백준 11660번 구간 합 구하기 5 실버 1

import sys

N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))

dp = [[0] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
  for j in range(1, N+1):
    dp[i][j] = graph[i-1][j-1] + dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]

for _ in range(M):
  r1, c1, r2, c2 = map(int, sys.stdin.readline().split())
  print(dp[r2][c2] - (dp[r2][c1 - 1] + dp[r1 - 1][c2]) + dp[r1 - 1][c1 - 1])
