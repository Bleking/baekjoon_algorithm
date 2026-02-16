# 백준 6236번 용돈 관리 실버 1

import sys

N, M = map(int, sys.stdin.readline().split())
money = []
for _ in range(N):
  money.append(int(sys.stdin.readline()))

pl, pr = max(money), sum(money)

answer = 0
while pl <= pr:
  pc = (pl + pr) // 2

  total = 0
  cnt = 1

  for i in range(N):
    if total + money[i] <= pc:
      total += money[i]
    else:
      total = money[i]
      cnt += 1

  if cnt < M:
    answer = pc
    pr = pc - 1
  elif cnt > M:
    pl = pc + 1
  elif cnt == M:
    answer = pc
    pr = pc - 1

print(answer)
