# 백준 1922번 네트워크 연결 골드 4

import sys
sys.setrecursionlimit(10 ** 6)

def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])

  return parent[x]

def union_parent(parent, a, b):
  a_parent = find_parent(parent, a)
  b_parent = find_parent(parent, b)

  if a_parent < b_parent:
    parent[b_parent] = a_parent
  else:
    parent[a_parent] = b_parent

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

edges = []
for _ in range(M):
  a, b, c = map(int, sys.stdin.readline().split())
  edges.append((c, a, b))

parent = [0] * (N+1)
for i in range(1, N+1):
  parent[i] = i

edges.sort()

answer = 0
for cost, A, B in edges:
  if find_parent(parent, A) != find_parent(parent, B):
    union_parent(parent, A, B)
    answer += cost

print(answer)
