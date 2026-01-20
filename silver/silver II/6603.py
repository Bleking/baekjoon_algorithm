# 백준 6603번 로또 실버 2

import sys
from itertools import combinations

T = []
while True:
  num_list = list(map(int, sys.stdin.readline().split()))
  if num_list[0] == 0:
    break
  T.append(num_list)

for t in T:
  nCr = combinations(t[1:t[0] + 1], 6)

  for i in list(nCr):
    print(*i)
  print()
