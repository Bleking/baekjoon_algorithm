# 백준 4963번 섬의 개수 실버 2

import sys
sys.setrecursionlimit(10 ** 4)

def DFS(graph, x, y):
  visited[y][x] = True

  dx = [ 0, 0, -1, 1, -1,  1,  -1, 1]
  dy = [-1, 1,  0, 0, -1, -1,  1, 1]

  for d in range(8):
    nx = x + dx[d]
    ny = y + dy[d]

    if 0 <= nx < w and 0 <= ny < h:
      if visited[ny][nx] == False and graph[ny][nx] == 1:
        DFS(graph, nx, ny)


while True:
  w, h = map(int, sys.stdin.readline().split())
  
  if w == 0 and h == 0:
    break
  
  landNsea = []
  for _ in range(h):
    landNsea.append(list(map(int, sys.stdin.readline().split())))

  visited = [[False] * w for _ in range(h)]

  answer = 0
  for x in range(w):
    for y in range(h):
      if visited[y][x] == False and landNsea[y][x] == 1:
        DFS(landNsea, x, y)
        answer += 1

  print(answer)
