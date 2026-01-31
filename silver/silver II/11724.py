# 백준 11724번 연결 요소의 개수 실버 2

import sys
sys.setrecursionlimit(10 ** 4)

N, M = map(int, sys.stdin.readline().split())  # node, edge

graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())  # node1, node2
  graph[u].append(v)
  graph[v].append(u)

visited = [False] * (N+1)

def dfs(graph, node, visited):
  visited[node] = True

  for n in graph[node]:
    if not visited[n]:
      dfs(graph, n, visited)

answer = 0
for n in range(1, N+1):
  if not visited[n]:
    dfs(graph, n, visited)
    answer += 1

print(answer)
