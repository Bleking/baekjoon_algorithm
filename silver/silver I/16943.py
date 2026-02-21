# 백준 16943번 숫자 재배치 실버 1

import sys
from itertools import permutations

A, B = map(str, sys.stdin.readline().strip().split())

answer = -1
for p in permutations(A, len(A)):
  C = ''.join(p)
  if C[0] != '0':
    if int(C) < int(B):
      answer = max(int(C), answer)

print(answer)
