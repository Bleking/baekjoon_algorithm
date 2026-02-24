# 백준 11659번 구간 합 구하기 4 실 3

import sys

N, M = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

sum_list = [0]
total = 0
for i in range(N):
  total += num_list[i]
  sum_list.append(total)

for _ in range(M):
  i, j = map(int, sys.stdin.readline().split())
  print(sum_list[j] - sum_list[i-1])
