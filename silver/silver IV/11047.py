# 백준 11047번 동전 0 실버 4

import sys

N, K = map(int, sys.stdin.readline().split())
coins = []
for _ in range(N):
  coins.append(int(sys.stdin.readline()))

coins.sort(reverse=True)

answer = 0
for i in range(len(coins)):
  if coins[i] <= K:
    answer += (K // coins[i])
    K %= coins[i]

print(answer)
