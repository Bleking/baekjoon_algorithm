# 백준 21736번 헌내기는 친구가 필요해 실버 2

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

campus_map = []
for n in range(N):
  row = list(map(str, sys.stdin.readline().strip()))
  if 'I' in row:
    start = (n, row.index('I'))
  campus_map.append(row)

x, y = start[0], start[1]

def campus_BFS(N, M, x, y):
  dx = [-1, 1, 0, 0]
  dy = [0, 0, -1, 1]

  queue = deque()
  queue.append((x, y))  # I가 있는 위치

  answer = 0
  while queue:
    x, y = queue.popleft()

    for d in range(4):
      nx = x + dx[d]
      ny = y + dy[d]

      if nx < 0 or nx >= N or ny < 0 or ny >= M:  # 범위를 벗어난 곳은 접근 불가
        continue
      
      if campus_map[nx][ny] == 'X':  # 벽은 접근 불가
        continue
      
      if campus_map[nx][ny] == 'O':  # 빈 공간일 때만 접근 가능
        campus_map[nx][ny] = 'Y'
        queue.append((nx, ny))

      elif campus_map[nx][ny] == 'P':  # 주의할 부분
        campus_map[nx][ny] = 'Y'
        queue.append((nx, ny))
        answer += 1

  return answer

result = campus_BFS(N, M, x, y)
if result == 0:
  print('TT')
else:
  print(result)
