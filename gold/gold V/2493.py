# 백준 2493번  골드 5

import sys

N = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

stack = []
answer = []

for i in range(N):
  while stack:
    if stack[-1][1] < towers[i]:
      stack.pop()
    else:
      answer.append(stack[-1][0])
      break
  if len(stack) == 0:
    answer.append(0)
  
  stack.append((i+1, towers[i]))

print(*answer)
