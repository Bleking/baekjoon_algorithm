# 백준 6118번 숨바꼭질 실버 1

import sys

from collections import deque

N, M = map(int, sys.stdin.readline().split())  # 노드 개수, 엣지 개수

graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [-1] * (N+1)

def bfs(graph, start, visited):
  queue = deque()
  queue.append(start)
  visited[start] = 0

  while queue:
    node = queue.popleft()

    for next in graph[node]:
      if visited[next] == -1:
        visited[next] = visited[node] + 1
        queue.append(next)

bfs(graph, 1, visited)

print(visited.index(max(visited)), max(visited), visited.count(max(visited)))
