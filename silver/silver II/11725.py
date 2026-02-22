# 백준 11725번 트리의 부모 찾기 실버 2

import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)
  graph[v].append(u)

def bfs(graph, node, parent, visited):
  queue = deque()
  queue.append(node)

  visited[node] = True

  while queue:
    node = queue.popleft()

    for next in graph[node]:
      if visited[next] == False:
        visited[next] = True
        parent[next] = node  # 부모 노드 기록
        queue.append(next)

visited = [False] * (N+1)
parent = [0] * (N+1)  # 부모 노드 저장

bfs(graph, 1, parent, visited)  # 1번이 루트 노드

for i in range(2, N+1):
  print(parent[i])
