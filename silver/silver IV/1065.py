# 백준 1065번 한수 실버4

import sys

N = int(sys.stdin.readline())

if N < 100:
  print(N)
else:
  count = 99
  for num in range(100, N+1):
    num = str(num)
    if (int(num[0]) - int(num[1])) == (int(num[1]) - int(num[2])):
      count += 1
  print(count)
