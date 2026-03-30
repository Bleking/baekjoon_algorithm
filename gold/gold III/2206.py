# 백준 2206번 벽 부수고 이동하기 골드 3

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[[False] * 2 for _ in range(M)] for _ in range(N)]

# 벽을 부순 개수를 확인하는 변수도 추가하자. 1로 설정해서 한번 감소하면 더이상 1인 부분을 뚫을 수 없도록.
def bfs(graph, r, c, visited):
  queue = deque()
  queue.append((r, c, 1, 1))  # 행렬 위치, 벽부수기 한도, 이동 거리

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  visited[r][c][1] = True

  while queue:
    r, c, b, move = queue.popleft()  # 행렬 위치, 벽부수기 한도

    if r == N - 1 and c == M - 1:
      return move

    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < N and 0 <= nc < M:
        if visited[nr][nc][b] == False:
          if graph[nr][nc] == 1:
            if b > 0:
              visited[nr][nc][b] = True
              queue.append((nr, nc, b-1, move + 1))
          if graph[nr][nc] == 0:
            visited[nr][nc][b] = True
            queue.append((nr, nc, b, move + 1))

  return -1

print(bfs(graph, 0, 0, visited))
