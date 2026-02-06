# 백준 2468번 안전 영역 실버 1

import sys
from collections import deque

N = int(sys.stdin.readline())

height = 0
graph = []
for i in range(N):
  graph.append(list(map(int, sys.stdin.readline().split())))

  for j in range(N):
    if graph[i][j] > height:
      height = graph[i][j]

def bfs(graph, start_r, start_c, height, visited):
  queue = deque()
  queue.append((start_r, start_c))
  
  visited[start_r][start_c] = True

  dr = [-1, 1,  0, 0]
  dc = [0, 0,  -1, 1]
  
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
for h in range(height):
  visited = [[False] * N for _ in range(N)]

  cnt = 0
  for i in range(N):
    for j in range(N):
      if visited[i][j] == False and graph[i][j] > h:
        bfs(graph, i, j, h, visited)
        cnt += 1
  answer.append(cnt)

print(max(answer))
