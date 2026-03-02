# 백준 16948번 데스 나이트 실버 1

import sys
from collections import deque

N = int(sys.stdin.readline())
r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

graph = [[0] * N for _ in range(N)]
visited = [[-1] * N for _ in range(N)]

def bfs(graph, r1, c1, r2, c2, visited):
  queue = deque()
  queue.append((r1, c1))

  visited[r1][c1] = 0

  dr = [-2, -2,  0, 0,  2, 2]
  dc = [-1,  1, -2, 2, -1, 1]
  
  while queue:
    r, c = queue.popleft()

    for d in range(6):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < N and 0 <= nc < N:
        if visited[nr][nc] == -1 and graph[nr][nc] == 0:
          queue.append((nr, nc))
          graph[nr][nc] = graph[r][c] + 1
          visited[nr][nc] = visited[r][c] + 1
  
  return graph[r2][c2]

bfs(graph, r1, c1, r2, c2, visited)

print(visited[r2][c2])
