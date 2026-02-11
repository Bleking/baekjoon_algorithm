# 백준 1654번 랜선 자르기 실버 2

import sys

K, N = map(int, sys.stdin.readline().split())

lines = []
for _ in range(K):
  lines.append(int(sys.stdin.readline()))

pl, pr = 1, max(lines)

answer = 0
while pl <= pr:
  pc = (pl + pr) // 2

  sum = 0
  for i in lines:
    sum += (i // pc)

  if sum < N:
    pr = pc - 1
  elif sum >= N:
    answer = pc
    pl = pc + 1

print(answer)
