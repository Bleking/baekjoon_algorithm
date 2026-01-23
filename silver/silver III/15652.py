# 백준 15652번 	N과 M (4) 실버 3

import sys
from itertools import combinations_with_replacement

N, M = map(int, sys.stdin.readline().split())
num_list = [_ for _ in range(1, N+1)]
nCr = combinations_with_replacement(num_list, M)

for i in nCr:
    print(*i)
