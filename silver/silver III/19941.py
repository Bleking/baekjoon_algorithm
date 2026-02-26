# 백준 19941번 햄버거 분배 실버 3

import sys

N, K = map(int, sys.stdin.readline().split())
table = list(map(str, sys.stdin.readline().strip()))

answer = 0
for i in range(N):
  if table[i] == 'P':
    for j in range(max(0, i-K), min(N, i+K+1)):
      if table[j] == 'H':
        table[j] = 'X'
        answer += 1
        break

print(answer)
