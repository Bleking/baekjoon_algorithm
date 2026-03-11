# 백준 7576번 토마토 골드 5

import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())

visited = [[False] * M for _ in range(N)]
graph = []
queue = deque()

for i in range(N):
  row = list(map(int, sys.stdin.readline().split()))
  graph.append(row)

  for j in range(M):
    if row[j] == 1:
      queue.append((i, j))
      visited[i][j] = True

def bfs(graph, queue):
  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  while queue:
    r, c = queue.popleft()
    
    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < N and 0 <= nc < M:
        if visited[nr][nc] == False and graph[nr][nc] == 0:
          queue.append((nr, nc))
          visited[nr][nc] = True
          graph[nr][nc] = graph[r][c] + 1

bfs(graph, queue)

answer = 0
for g in graph:
  answer = max(answer, max(g))

  if 0 in g:
    answer = 0
    break

print(answer - 1)
