# 백준 15651번 N과 M (3) 실버 3

import sys
from itertools import product

N, M = map(int, sys.stdin.readline().split())
num_list = [_ for _ in range(1, N+1)]

prod = product(num_list, repeat=M)
for i in prod:
    print(*i)
