# 백준 2644번 촌수계산 실버 2

import sys
from collections import deque

n = int(input())  # 노드 개수
start, end = map(int, sys.stdin.readline().split())
m = int(input())  # edge 개수

graph = [[] for _ in range(n + 1)]
for _ in range(m):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

visited = [-1] * (n + 1)

def bfs(graph, start, end, visited):
  queue = deque()
  queue.append(start)
  visited[start] = 0

  while queue:
    node = queue.popleft()

    if node == end:
      break

    for next in graph[node]:
      if visited[next] == -1:
        visited[next] = visited[node] + 1
        queue.append(next)

bfs(graph, start, end, visited)

print(visited[end])
