# 백준 13706번 제곱근 실버 4

import sys

N = int(sys.stdin.readline())

pl, pr = 1, N
while pl <= pr:
  pc = (pl + pr) // 2

  square = pc ** 2

  if square < N:
    pl = pc + 1
  elif square > N:
    pr = pc - 1
  elif square == N:
    answer = pc
    break

print(answer)
