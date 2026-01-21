# 백준 10819번 차이를 최대로 실버 2

import sys
from itertools import permutations

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

max_sum = 0
perm = permutations(num_list, N)  # 그냥 순열 돌려서 찾는다.
for i in perm:
  sum = 0
  for j in range(1, N):
    sum += abs(i[j] - i[j-1])
  
  if max_sum < sum:
    max_sum = sum
  
print(max_sum)
