# 백준 16953번 A → B 실버 2 (BFS 미사용)

import sys

A, B = map(int, sys.stdin.readline().split())

count = 1
while B != A:
  if B < A:
    count = -1
    break
  
  if B % 2 == 0:
    B = B // 2
  elif B % 10 == 1:
    B = B // 10
  else:
    count = -1
    break
  
  count += 1

print(count)
