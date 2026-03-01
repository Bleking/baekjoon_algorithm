# 백준 14940번 쉬운 최단거리 실버 1

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())  # 세로, 가로

graph = []
for r in range(n):
  row = list(map(int, sys.stdin.readline().split()))
  graph.append(row)
  if 2 in row:
    a, b = r, row.index(2)

def bfs(graph, r, c, visited):
  queue = deque()
  queue.append((r, c))

  visited[r][c] = 0

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  while queue:
    r, c = queue.popleft()

    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < n and 0 <= nc < m:
        if visited[nr][nc] == -1 and graph[nr][nc] != 0:
          queue.append((nr, nc))
          visited[nr][nc] = visited[r][c] + 1

visited = [[-1] * m for _ in range(n)]
for i in range(n):
  for j in range(m):
    if graph[i][j] == 0:
      visited[i][j] = 0

bfs(graph, a, b, visited)
for v in visited:
  print(*v)
