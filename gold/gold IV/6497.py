# 백준 6497번 전력난 골드 4

import sys

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

while True:
  m, n = map(int, sys.stdin.readline().split())  # 집의 수, 길의 수
  if m == 0 and n == 0:
    break

  parent = [0] * m
  for i in range(m):
    parent[i] = i

  edges = []
  for _ in range(n):
    x, y, z = map(int, sys.stdin.readline().split())  # x, y번 집 사이에 길이가 z인 길이 있다.
    edges.append((z, x, y))
    
  edges.sort()  # 가중치순으로 정렬

  answer = 0
  for cost, a, b, in edges:
    if find_parent(parent, a) != find_parent(parent, b):
      union_parent(parent, a, b)
    else:
      answer += cost
  
  print(answer)
