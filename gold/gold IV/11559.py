# 백준 11559번 Puyo Puyo 골드 4

import sys
from collections import deque

field = []
for _ in range(12):
  field.append(list(sys.stdin.readline().strip()))

def bfs(graph, r, c, color, visited):
  queue = deque()
  queue.append((r, c))

  same_color = []
  same_color.append((r, c))

  visited[r][c] = True

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  while queue:
    r, c = queue.popleft()

    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < 12 and 0 <= nc < 6:
        if visited[nr][nc] == False and graph[nr][nc] == color:
          visited[nr][nc] = True

          queue.append((nr, nc))
          same_color.append((nr, nc))

  return same_color

def fall():
    for c in range(6):
        blocks = deque()

        # 1. 아래에서 위로 보면서 블록만 수집
        for r in range(12 - 1, -1, -1):
            if field[r][c] != '.':  # 빈칸이 아니면 블록
                blocks.append(field[r][c])

        # 2. 해당 열 전체를 빈칸으로 초기화
        for r in range(12):
            field[r][c] = '.'

        # 3. 아래에서부터 다시 채우기
        nr = 11
        while blocks:
            field[nr][c] = blocks.popleft()
            nr -= 1

answer = 0
while True:
  visited = [[False] * 6 for _ in range(12)]
  blow_up = []
  flag = False

  for i in range(12):
    for j in range(6):
      if visited[i][j] == False and field[i][j] != '.':
        same_color = bfs(field, i, j, field[i][j], visited)

        if len(same_color) >= 4:
          blow_up += same_color
          flag = True
  
  for r, c in blow_up:
    field[r][c] = '.'

  if flag == True:
    answer += 1

  fall()

  if not blow_up:
    break

print(answer)
