# 백준 10451번 순열 사이클 실버 3

import sys
from collections import deque

def bfs(graph, node, visited):
  queue = deque()
  queue.append(node)

  visited[node] = True
  
  while queue:
    node = queue.popleft()

    for next in graph[node]:
      if visited[next] == False:
        queue.append(next)
        visited[next] = True

T = int(sys.stdin.readline())
for t in range(T):
  N = int(sys.stdin.readline())
  nodes = list(map(int, sys.stdin.readline().split()))

  graph = [[] for _ in range(N+1)]
  for i in range(N):
    graph[i+1].append(nodes[i])
    graph[nodes[i]].append(i+1)

  visited = [False] * (N+1)

  answer = 0
  for i in range(1, N+1):
    if visited[i] == False:
      bfs(graph, i, visited)
      answer += 1

  print(answer)
