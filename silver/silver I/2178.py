# 백준 2178번 	미로 탐색 실버 1

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

maze = []
for n in range(N):
  maze.append(list(map(int, sys.stdin.readline().strip())))

def maze_BFS(N, M, x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  queue = deque()
  queue.append((x, y))

  while queue:
    x, y = queue.popleft()

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위를 벗어난 곳은 접근 불가
        continue

      if maze[nx][ny] == 0:  # 0인 곳은 접근 불가
        continue

      if maze[nx][ny] == 1:  # 1일 때만 접근 가능
        maze[nx][ny] = maze[x][y] + 1
        queue.append((nx, ny))  #

  return maze[N-1][M-1]

print(maze_BFS(N, M, 0, 0))
