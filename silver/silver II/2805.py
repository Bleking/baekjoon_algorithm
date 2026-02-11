# 백준 2805번 나무 자르기 실버 2

import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))

pl, pr = 0, max(tree)

while pl <= pr:
  sum = 0
  pc = (pl + pr) // 2

  for t in tree:
    if t > pc:
      sum += (t - pc)

  if sum < M:
    pr = pc -1
  elif sum >= M:
    pl = pc + 1
    answer = pc

print(answer)
