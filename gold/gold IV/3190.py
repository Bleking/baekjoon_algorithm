# 백준 3190번 뱀 골드 4 

import sys
from collections import deque

N = int(sys.stdin.readline())  # 보드 크기

K = int(sys.stdin.readline())  # 사과 개수
apples = []
for _ in range(K):
  r, c = map(int, sys.stdin.readline().split())
  apples.append([r, c])

L = int(sys.stdin.readline())  # 방향 변환 횟수
directions = []
dir_idx = 0
for _ in range(L):
  X, C = map(str, sys.stdin.readline().split())
  directions.append([int(X), C])

graph = [[0] * N for _ in range(N)]
for a1, a2 in apples:
  graph[a1 - 1][a2 - 1] = 4

r, c = 0, 0

snake = deque()
snake.append([r, c])
graph[r][c] = 1  # 뱀의 초기 위치

dr = [0, 1,  0, -1]  # 오른, 아래, 왼, 위
dc = [1, 0, -1,  0]
d = 0  # 방향 인덱스
dir_idx = 0  # directions의 인덱스

answer = 0  # 경과한 시간
while True:
  answer += 1

  r += dr[d]
  c += dc[d]

  if not (0 <= r < N and 0 <= c < N):
    break
  
  # 뱀이 그냥 지나감
  if graph[r][c] == 0:
    # 이동한 위치를 1로 표기
    graph[r][c] = 1
    snake.append([r, c])

    # 전 위치는 0으로 변환
    prev_r, prev_c = snake.popleft()
    graph[prev_r][prev_c] = 0

  # 사과 먹기
  elif graph[r][c] == 4:
    snake.append([r, c])
    graph[r][c] = 1  # 사과는 먹었으니 사라짐

  else:  # 사과도 아닌 빈칸도 아닌 곳에 부딛히면. 즉, 자기 몸에 부딛히면
    break  # 종료
  
  if answer == directions[dir_idx][0]:
    if directions[dir_idx][1] == 'D':
      d = (d + 1) % 4
    elif directions[dir_idx][1] == 'L':
      d = (d - 1) % 4

    if dir_idx < L - 1:
      dir_idx += 1

print(answer)
