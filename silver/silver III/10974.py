# 백준 10974번 모든 순열 실버 3

import sys
from itertools import permutations

N = int(sys.stdin.readline())
iter = permutations(range(1, N+1), N)

for i in iter:
  print(*i)
