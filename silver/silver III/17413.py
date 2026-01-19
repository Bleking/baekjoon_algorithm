# 백준 17413번 단어 뒤집 실버3

import sys

S = sys.stdin.readline().strip()

reverse = True
stack = []
answer = []

for s in S:
  if s == '<':
    reverse = False
    for _ in range(len(stack)):
      answer.append(stack.pop())
  
  stack.append(s)

  if s == '>':
    reverse = True
    for _ in range(len(stack)):
      answer.append(stack.pop(0))

  if s == ' ' and reverse == True:
    for i in range(len(stack)):
      if i == 0:
        stack.pop()
        continue
      answer.append(stack.pop())
    answer.append(' ')

if stack:
  for idx in range(len(stack)):
    answer.append(stack.pop())

for a in answer:
  print(a, end="")
