# 백준 1753번 최단경로 골드 4

import sys
import heapq

INF = int(1e9)

V, E = map(int, sys.stdin.readline().split())  # 노드, 엣지
S = int(sys.stdin.readline())  # 시작 노드

graph = [[] for _ in range(V+1)]
for _ in range(E):
  u, v, w = map(int, sys.stdin.readline().split())
  graph[u].append((v, w))

distance = [INF] * (V+1)

def dijkstra(node, distance):
  heap = []

  heapq.heappush(heap, (0, node))
  distance[node] = 0

  while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
      continue
    
    for g in graph[now]:
      cost = dist + g[1]

      if cost < distance[g[0]]:
        distance[g[0]] = cost
        heapq.heappush(heap, (cost, g[0]))

dijkstra(S, distance)

for i in range(1, V+1):
  if distance[i] == INF:
    print('INF')
  else:
    print(distance[i])
