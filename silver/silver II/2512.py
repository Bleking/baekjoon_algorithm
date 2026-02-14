# 백준 2512번 예산 실버 2

import sys

N = int(sys.stdin.readline())
budgets = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())

pl, pr = 1, max(budgets)

answer = 0
while pl <= pr:
  pc = (pl + pr) // 2

  total = 0
  for i in range(N):
    if budgets[i] > pc:
      total += pc
    else:
      total += budgets[i]

  if total <= M:
    answer = pc
    pl = pc + 1
  else:
    pr = pc - 1

print(answer)
