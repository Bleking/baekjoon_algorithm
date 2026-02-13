# 백준 2470번 두 용액 골드 5

import sys

N = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()

liquid.sort()

pl, pr = 0, N-1
ans_left, ans_right = pl, pr

answer = abs(liquid[pl] + liquid[pr])

while pl < pr:
  sum = liquid[pl] + liquid[pr]

  if abs(sum) < answer:
    answer = abs(sum)

    ans_left = pl
    ans_right = pr

    if answer == 0:
      break

  if sum < 0:
    pl += 1
  else:
    pr -= 1

print(liquid[ans_left], liquid[ans_right])
