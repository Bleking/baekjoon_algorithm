# 백준 15650번 N과 M (2) 실버 3

import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
num_list = [_ for _ in range(1, N+1)]

comb = combinations(num_list, M)
for i in comb:
    print(*i)
