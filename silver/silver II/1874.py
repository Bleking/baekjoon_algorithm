# 백준 1874번 스택 수열 실버 2

import sys

n = int(sys.stdin.readline())

stack = []
answer = []

curr = 1
status = True

for i in range(n):
  num = int(sys.stdin.readline())

  while num >= curr:
    answer.append('+')
    stack.append(curr)
    curr += 1
  
  if stack[-1] == num:
    stack.pop()
    answer.append('-')
  else:
    status = False

if status:
  for a in answer:
    print(a)
else:
  print('NO')
