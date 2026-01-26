# 백준 2606번 바이러스 실버 3

import sys

def virus_DFS(graph, start):
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

  return len(visited[1:])


node = int(sys.stdin.readline())
edge = int(sys.stdin.readline())

tree = {}
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

print(virus_DFS(tree, 1))
