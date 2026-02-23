# 백준 1389번 케빈 베이컨의 6단계 법칙 실버 1

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

def bfs(graph, node, visited):
  queue = deque()
  queue.append(node)

  visited[node] = 0

  while queue:
    node = queue.popleft()

    for next in graph[node]:
      if visited[next] == -1:
        queue.append(next)
        visited[next] = visited[node] + 1

answer = []
for i in range(1, N+1):
  visited = [-1] * (N+1)
  bfs(graph, i, visited)
  answer.append(sum(visited[1:]))

print(answer.index(min(answer)) + 1)
