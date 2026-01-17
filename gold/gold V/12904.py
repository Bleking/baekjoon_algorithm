# 백준 12904번 A와 B 골드5

import sys

S = list(map(str, sys.stdin.readline().strip()))
T = list(map(str, sys.stdin.readline().strip()))

while len(S) < len(T):
  if T[-1] == 'A':
    T.pop()
  elif T[-1] == 'B':
    T.pop()
    T = T[::-1]

if S == T:
  print(1)
else:
  print(0)
