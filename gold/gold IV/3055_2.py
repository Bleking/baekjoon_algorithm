# 백준 3055번 탈출 골드 4

import sys
from collections import deque

R, C = map(int, sys.stdin.readline().split())

graph = []
for i in range(R):
  row = list(sys.stdin.readline().strip())
  graph.append(row)
  for j in range(C):
    if row[j] == 'S':
      S = [i, j]

water = deque()
for i in range(R):
  for j in range(C):
    if graph[i][j] == 'S':
      S = [i, j]
    if graph[i][j] == '*':
      water.append([i, j])

def bfs(graph, r, c, visited, water):
  # 고슴도치 위치 및 이동 거리
  queue = deque()
  queue.append((r, c, 0))  # 행렬 위치, 이동 거리

  visited[r][c] = True

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  while queue:
    # 물 확산
    for _ in range(len(water)):
      wr, wc = water.popleft()

      for d in range(4):
        nwr = wr + dr[d]
        nwc = wc + dc[d]

        if 0 <= nwr < R and 0 <= nwc < C:
          if graph[nwr][nwc] == '.':
            graph[nwr][nwc] = '*'
            water.append((nwr, nwc))
    
    # 고슴도치 이동
    for _ in range(len(queue)):
      r, c, move = queue.popleft()

      if graph[r][c] == 'D':
        return move
        
      for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]

        if 0 <= nr < R and 0 <= nc < C:
          if visited[nr][nc] == False and (graph[nr][nc] != 'X' and graph[nr][nc] != '*'):
            visited[nr][nc] = True
            queue.append((nr, nc, move + 1))
  
  return 'KAKTUS'

visited = [[False] * C for _ in range(R)]

print(bfs(graph, S[0], S[1], visited, water))
