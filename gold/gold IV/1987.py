# 백준 1987번 알파벳 골드 4

import sys
sys.setrecursionlimit(10 ** 4)

R, C = map(int, sys.stdin.readline().split())
graph = []
for _ in range(R):
  graph.append(list(sys.stdin.readline().strip()))

answer = 1
visited = set(graph[0][0])  # 방문한 알파벳 저장

def dfs(graph, r, c, visited, move):
  global answer
  answer = max(answer, move)

  dr = [-1, 1,  0, 0]
  dc = [ 0, 0, -1, 1]

  for d in range(4):
    nr = r + dr[d]
    nc = c + dc[d]

    if 0 <= nr < R and 0 <= nc < C:
      if graph[nr][nc] not in visited:
        visited.add(graph[nr][nc])  # 알파벳 추가
        dfs(graph, nr, nc, visited, move + 1)
        visited.remove(graph[nr][nc])  # 백트래킹: 원복

dfs(graph, 0, 0, visited, answer)

print(answer)
