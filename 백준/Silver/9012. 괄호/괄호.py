import sys

T = int(sys.stdin.readline())

for t in range(T):
  S = sys.stdin.readline().strip()
  stack = []

  for s in S:
    if s == '(':
      stack.append(s)
    elif s == ')':
      if stack and stack[-1] == '(':
        stack.pop()
      else:
        stack.append(s)
  
  if stack:
    print('NO')
  else:
    print('YES')