# 백준 2669번 직사각형 네개의 합집합의 면적 구하기 실버 5

import sys

graph = [[0] * 100 for _ in range(100)]

for _ in range(4):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  for y in range(y1, y2):
    for x in range(x1, x2):
      graph[y][x] = 1

answer = 0
for g in graph:
  answer += sum(g)

print(answer)
