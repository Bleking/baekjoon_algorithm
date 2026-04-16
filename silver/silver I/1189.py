# 백준 1189번 컴백 실버 1

import sys

R, C, K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
  graph.append(list(sys.stdin.readline().strip()))

def dfs(graph, r, c, move, visited):
  global answer  # 가짓 수

  visited[r][c] = True

  if move == K and r == 0 and c == C -1:
    answer += 1

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  for d in range(4):
    nr = r + dr[d]
    nc = c + dc[d]

    if 0 <= nr < R and 0 <= nc < C:
      if graph[nr][nc] == '.' and visited[nr][nc] == False:
        visited[nr][nc] = True
        dfs(graph, nr, nc, move + 1, visited)
        visited[nr][nc] = False

visited = [[False] * C for _ in range(R)]
 
answer = 0
dfs(graph, R-1, 0, 1, visited)
print(answer)
