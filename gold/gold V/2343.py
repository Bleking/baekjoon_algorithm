# 백준 2343번 	기타 레슨 골드 5

import sys

N, M = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))

pl, pr = max(lectures), sum(lectures)

answer = 0
while pl <= pr:
  pc = (pl + pr) // 2

  total = 0
  cnt = 1
  for i in range(N):
    if total + lectures[i] <= pc:
      total += lectures[i]
    else:
      total = lectures[i]
      cnt += 1
  
  if cnt > M:
    pl = pc + 1
  else:
    pr = pc - 1
    answer = pc

print(answer)
