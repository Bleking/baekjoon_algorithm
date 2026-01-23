# 백준 15649번 N과 M (1) 실버 3

import sys
from itertools import permutations

N, M = map(int, sys.stdin.readline().split())
num_list = [_ for _ in range(1, N+1)]

perm = permutations(num_list, M)
for i in perm:
    print(*i)
