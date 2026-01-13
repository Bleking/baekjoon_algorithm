# 백준 10799 쇠막대기 실버 2

import sys

rod = sys.stdin.readline().strip()

stack = []
cnt = 0

for i in range(len(rod)):
  if rod[i] == '(':
    stack.append('(')
  elif rod[i] == ')':
    stack.pop()
    if rod[i-1] == '(':
      cnt += len(stack)
    elif rod[i-1] == ')':
      cnt += 1

print(cnt)
