# 백준 2468번 안전 영역 실버 1

import sys
from collections import deque

N = int(sys.stdin.readline())

max_height = 0
graph = []
for i in range(N):
  row = list(map(int, sys.stdin.readline().split()))
  graph.append(row)
  if max_height < max(row):
    max_height = max(row)

def bfs(graph, r, c, visited, height):
  queue = deque()
  queue.append((r, c))

  visited[r][c] = True
  
  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  while queue:
    r, c = queue.popleft()

    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < N and 0 <= nc < N:
        if visited[nr][nc] == False and graph[nr][nc] > height:
          queue.append((nr, nc))
          visited[nr][nc] = True

answer = []
for h in range(max_height):
  visited = [[False] * N for _ in range(N)]
  cnt = 0
  for i in range(N):
    for j in range(N):
      if visited[i][j] == False and graph[i][j] > h:
        bfs(graph, i, j, visited, h)
        cnt += 1

  answer.append(cnt)

print(max(answer))
