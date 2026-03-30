# 백준 14442번 벽 부수고 이동하기 2 골드 3

import sys
from collections import deque

N, M, K = map(int, sys.stdin.readline().split())

graph = []
for _ in range(N):
  graph.append(list(map(int, sys.stdin.readline().strip())))

visited = [[[-1] * (K+1) for _ in range(M)] for _ in range(N)]

# 벽을 부순 개수를 확인하는 변수도 추가하자. 1로 설정해서 한번 감소하면 더이상 1인 부분을 뚫을 수 없도록.
def bfs(graph, r, c, visited):
  queue = deque()
  queue.append((r, c, K))  # 행렬 위치, 벽부수기 한도

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  visited[r][c][K] = 1

  while queue:
    r, c, b = queue.popleft()  # 행렬 위치, 벽부수기 한도

    if r == N - 1 and c == M - 1:
      return visited[r][c][b]

    for d in range(4):
      nr = r + dr[d]
      nc = c + dc[d]

      if 0 <= nr < N and 0 <= nc < M:
        if graph[nr][nc] == 1 and b > 0:  # 벽일 때, 그리고 벽 부수기 횟수가 남아있을 때
          nb = b - 1  # 벽 부수기 횟수 1회 감소
          if visited[nr][nc][nb] == -1:  # 벽을 부순 위치가 방문되지 않았다면
              visited[nr][nc][nb] = visited[r][c][b] + 1  # 방문
              queue.append((nr, nc, nb))
        if graph[nr][nc] == 0:  # 벽이 아닌 통로면
          if visited[nr][nc][b] == -1:  # 방문하지 않은 구간이면
            visited[nr][nc][b] = visited[r][c][b] + 1  # 그냥 방문한다.
            queue.append((nr, nc, b))

  return -1

print(bfs(graph, 0, 0, visited))
