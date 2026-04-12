# 백준 1952번 달팽이2 브론즈 1

import sys

M, N = map(int, sys.stdin.readline().split())

graph = []
for _ in range(M):
  graph.append([0] * N)

r, c = 0, 0

d = 0
dr = [0, 1,  0, -1]  # 우, 하, 좌, 상
dc = [1, 0, -1,  0]  # 우, 하, 좌, 상

num = 1

cnt = 0  # 회전 횟수
for i in range(M * N):
  graph[r][c] = num

  nr = r + dr[d]
  nc = c + dc[d]

  if not (0 <= nr < M and 0 <= nc < N and graph[nr][nc] == 0):
    d = (d + 1) % 4

    nr = r + dr[d]
    nc = c + dc[d]

    if num != M * N:
      cnt += 1

  num += 1
  
  r = nr
  c = nc

print(cnt)
