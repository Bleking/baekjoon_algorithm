# 백준 7562번 나이트의 이동 실버 1

import sys
from collections import deque

def bfs(graph, start_r, start_c, end_r, end_c, visited):
  queue = deque()
  queue.append((start_r, start_c))

  dr = [-1, -2, -2, -1,  1,  2, 2, 1]
  dc = [-2, -1,  1,  2, -2, -1, 1, 2]

  if start_r == end_r and start_c == end_c:
    return 0

  while queue:
    r, c = queue.popleft()

    for d in range(8):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < I and 0 <= nc < I:
        if visited[nr][nc] ==  False and graph[nr][nc] == 0:
          queue.append((nr, nc))
          visited[nr][nc] = True
          graph[nr][nc] = graph[r][c] + 1
        
        if nr == end_r and nc == end_c:
          return graph[nr][nc]

T = int(sys.stdin.readline())

for t in range(T):
  I = int(sys.stdin.readline())
  chess = [[0] * I for _ in range(I)]
  visited = [[False] * I for _ in range(I)]

  start_r, start_c = map(int, sys.stdin.readline().split())
  end_r, end_c = map(int, sys.stdin.readline().split())

  print(bfs(chess, start_r, start_c, end_r, end_c, visited))
