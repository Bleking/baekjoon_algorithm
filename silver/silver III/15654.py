# 백준 15654번 N과 M (5) 실버 3

import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

perm = permutations(sorted(num_list), M)

for i in perm:
  print(*i)
