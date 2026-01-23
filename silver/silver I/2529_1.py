# 백준 2529번 부등호 실버 1 (PyPy3)

import sys
from itertools import permutations

k = int(sys.stdin.readline())
brackets = list(map(str, sys.stdin.readline().split()))

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
perm = permutations(numbers, k+1)

answer = []
for p in perm:
  flag = 0
  for i in range(len(p) - 1):
    if brackets[i] == '<':
      if p[i] < p[i+1]:
        flag += 1
      else:
        break
    if brackets[i] == '>':
      if p[i] > p[i+1]:
        flag += 1
      else:
        break

    if flag == k:
      answer.append(p)

print(''.join(map(str, answer[-1])))
print(''.join(map(str, answer[0])))
