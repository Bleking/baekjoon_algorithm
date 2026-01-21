# 백준 1182번 부분수열의 합 실버 2

import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

answer = 0
for i in range(1, N+1):
  comb = combinations(num_list, i)
  for idx in comb:
    if sum(idx) == S:
      answer += 1

print(answer)
