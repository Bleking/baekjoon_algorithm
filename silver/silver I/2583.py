# 백준 2583번 	영역 구하기 실버 1

import sys
from collections import deque

M, N, K = map(int, sys.stdin.readline().split())

graph = [[0] * N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for _ in range(K):
  x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
  for y in range(y1, y2):
    for x in range(x1, x2):
      graph[y][x] = 1

def bfs(graph, r, c, visited):
  queue = deque()
  queue.append((r, c))

  cnt = 1

  visited[r][c] = True

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  while queue:
    r, c = queue.popleft()

    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < M and 0 <= nc < N:
        if visited[nr][nc] == False and graph[nr][nc] != 1:
          visited[nr][nc] = True
          queue.append((nr, nc))
          graph[nr][nc] = graph[r][c] + 1
          cnt += 1

  return cnt

cnt = 0
sizes = []
for i in range(M):
  for j in range(N):
    if visited[i][j] == False and graph[i][j] != 1:
      sizes.append(bfs(graph, i, j, visited))
      cnt += 1
        
sizes.sort()

print(cnt)
print(*sizes)
