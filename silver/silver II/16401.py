# 백준 16401번 과자 나눠주기 실버 2

import sys

M, N = map(int, sys.stdin.readline().split())
cookies = list(map(int, sys.stdin.readline().split()))

pl, pr = 1, max(cookies)

answer = 0
while pl <= pr:
  pc = (pl + pr) // 2

  cnt = 0
  for i in range(N):
    if cookies[i] >= pc:
      cnt += (cookies[i] // pc)

  if cnt >= M:
    answer = pc
    pl = pc + 1
  else:
    pr = pc - 1

print(answer)
