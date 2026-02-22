# 백준 1407번 	2로 몇 번 나누어질까 골드 4

import sys

A, B = map(int, sys.stdin.readline().split())

def f(N):
  if N == 0:
    return 0

  answer = 0
  power = 1

  while power <= N:
    cnt = (N // power) - (N // (power * 2))
    answer += (cnt * power)
    power *= 2

  return answer

print(f(B) - f(A-1))
