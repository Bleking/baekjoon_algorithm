import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

def bfs(graph, r, c, visited):
  queue = deque()
  queue.append((r, c))
  
  visited[r][c] = True

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  cnt = 1
  while queue:
    r, c = queue.popleft()

    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < n and 0 <= nc < m:
        if visited[nr][nc] == False and graph[nr][nc] == 1:
          queue.append((nr, nc))
          visited[nr][nc] = True
          cnt += 1

  return cnt

visited = [[False] * m  for _ in range(n)]

answer = []
cnt = 0
for i in range(n):
  for j in range(m):
    if visited[i][j] == False and graph[i][j] == 1:
      cnt += 1
      answer.append(bfs(graph, i, j, visited))

print(cnt)
if cnt == 0:
  print(0)
else:
  print(max(answer))