# 백준 13164번 행복 유치원 골드5

import sys

N, K = map(int, sys.stdin.readline().split())
kinder = list(map(int, sys.stdin.readline().split()))

difs = []
for i in range(1, N):
  difs.append(kinder[i] - kinder[i-1])

difs.sort()

print(sum(difs[:N-K]))
