# 백준 3886번 좋은 단어 실버 4

import sys

N = int(sys.stdin.readline())

answer = 0
for n in range(N):
  word = sys.stdin.readline().strip()
  stack = []

  for w in word:
    if stack and stack[-1] == w:
      stack.pop()
    else:
      stack.append(w)
  
  if len(stack) == 0:
    answer += 1

print(answer)
