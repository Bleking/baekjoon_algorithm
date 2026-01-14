# 백준 9009번 피보나치 실버1

import sys

fibo = [0, 1]
for f in range(2, 46):
  fibo.append(fibo[f-1] + fibo[f-2])

T = int(sys.stdin.readline())
for t in range(T):
  n = int(sys.stdin.readline())

  answer = []
  for i in range(45, 0, -1):
    if fibo[i] <= n:
      answer.append(fibo[i])
      n -= fibo[i]

  answer = sorted(answer)

  for a in answer:
    print(a, end=' ')
