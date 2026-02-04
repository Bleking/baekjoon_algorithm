# 백준 1926번 그림 실버 1

import sys
sys.setrecursionlimit(10 ** 6)

def DFS(graph, x, y, n, m):  # x: 너비, y: 높이
  visited[y][x] = True

  dx = [ 0, 0, -1, 1]  # 상, 하, 좌, 우
  dy = [-1, 1,  0, 0]  # 상, 하, 좌, 우

  cnt = 1
  for d in range(4):
    nx = x + dx[d]  # 너비 이동
    ny = y + dy[d]  # 높이 이동

    if 0 <= nx < m and 0 <= ny < n:  # 범위 내
      if graph[ny][nx] == 1 and visited[ny][nx] == False:
        cnt += DFS(graph, nx, ny, n, m)
  
  return cnt


n, m = map(int, sys.stdin.readline().split())  # 세로 가로

graph = []
for _ in range(n):
  graph.append(list(map(int, sys.stdin.readline().split())))

visited = [[False] * m for _ in range(n)]

num_paint = 0
sizes = []
for x in range(m):
  for y in range(n):
    if visited[y][x] == False and graph[y][x] == 1:
      # print(DFS(graph, x, y, n, m))
      sizes.append(DFS(graph, x, y, n, m))
      num_paint += 1

print(num_paint)
if num_paint == 0:
  print(0)
else:
  print(max(sizes))
