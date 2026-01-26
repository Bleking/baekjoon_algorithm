# 백준 1260번 DFS와 BFS 실버 2

import sys
from collections import deque

def BFS(graph, start):
  visited = []  # visited[node] = True: 방문한 노드
  queue = deque([start])

  while queue:
    node = queue.popleft()

    if node not in visited:
      visited.append(node)

      if node in graph:
        temp = list(set(graph[node]) - set(visited))
        temp.sort()

        queue += temp

  return " ".join(str(i) for i in visited)

def DFS(graph, start):
  visited = []
  stack = [start]

  while stack:
    node = stack.pop()
    if node not in visited:
      visited.append(node)
      if node in graph:
        temp = list(set(graph[node])- set(visited))
        temp.sort(reverse=True)  # 왼쪽 노드를 먼저 들려야 하는데 stack 특성상 가장 최근에 들어온게 먼저 나가야 해서

        stack += temp

  return " ".join(str(i) for i in visited)

tree = {}
node, edge, start = map(int, sys.stdin.readline().split())
for i in range(edge):
  node1, node2 = map(int, sys.stdin.readline().split())

  if node1 not in tree:
    tree[node1] = [node2]
  elif node2 not in tree[node1]:
    tree[node1].append(node2)

  if node2 not in tree:
    tree[node2] = [node1]
  elif node1 not in tree[node2]:
    tree[node2].append(node1)

    
print(DFS(tree, start))
print(BFS(tree, start))
