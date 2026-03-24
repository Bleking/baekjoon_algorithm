# 백준 3584번 가장 가까운 공통 조상 골드 4

import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
  N = int(sys.stdin.readline())

  d = [0] * (N+1)
  c = [0] * (N+1)
  parent = [0] * (N+1)

  graph = [[] for _ in range(N+1)]
  children = set()  # 자식 노드

  for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    children.add(b)

  # 루트 노드 결정하기 (한번도 자식 노드가 아니었던 노드)
  root = 0
  for n in range(1, N+1):
    if n not in children:
      root = n
      break

  def bfs(root):
    queue = deque()
    queue.append(root)

    c[root] = True
    while queue:
      node = queue.popleft()

      for next in graph[node]:
        if c[next] == True:
          continue

        queue.append(next)
        parent[next] = node
        c[next] = True
        d[next] = d[node] + 1

  def LCA(a, b):
    while d[a] != d[b]:
      if d[a] > d[b]:
        a = parent[a]
      else:
        b = parent[b]

    while a != b:
      a = parent[a]
      b = parent[b]

    return a
      
  bfs(root)

  a, b = map(int, sys.stdin.readline().split())
  print(LCA(a, b))
