# 백준 1197번 최소 스패닝 트리 골드 4

import sys
sys.setrecursionlimit(10 ** 6)

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])

  return parent[x]

def union_parent(parent, a, b):
  a_parent = find_parent(parent, a)
  b_parent = find_parent(parent, b)

  if a_parent > b_parent:
    parent[a_parent] = b_parent
  else:
    parent[b_parent] = a_parent

V, E = map(int, sys.stdin.readline().split())

parent = [0] * (V+1)
for i in range(V):
  parent[i] = i

edges = []
for _ in range(E):
  A, B, C = map(int, sys.stdin.readline().split())
  edges.append((C, A, B))

edges.sort()

answer = 0
for cost, a, b in edges:
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    answer += cost

print(answer)
