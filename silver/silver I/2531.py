# 백준 2531번 회전 초밥 실버 1

import sys

N, d, k, c = map(int, sys.stdin.readline().split())
sushi = []
for _ in range(N):
  sushi.append(int(sys.stdin.readline()))

sushi += sushi[:k]

answer = 0
for i in range(N):
  sushi_set = set(sushi[i:i+k])
  sushi_set.add(c)
  answer = max(answer, len(sushi_set))

print(answer)
