# 백준 14716번 현수막 실버 1

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())  # 행, 열
graph = []
for _ in range(M):
  graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * N for _ in range(M)]

def bfs(graph, r, c, visited):
  queue = deque()
  queue.append((r, c))
  visited[r][c] = True

  dr = [-1, 1,  0, 0, -1, -1,  1, 1]  # 상, 하, 좌, 우, 상좌, 상우, 하좌, 하우
  dc = [ 0, 0, -1, 1, -1,  1, -1, 1]  # 상, 하, 좌, 우, 상좌, 상우, 하좌, 하우

  while queue:
    r, c = queue.popleft()

    for d in range(8):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < M and 0 <= nc < N:
        if visited[nr][nc] == False and graph[nr][nc] == 1:
          visited[nr][nc] = True
          queue.append((nr, nc))

cnt = 0
for i in range(M):
  for j in range(N):
    if visited[i][j] == False and graph[i][j] == 1:
      bfs(graph, i, j, visited)
      cnt += 1

print(cnt)
