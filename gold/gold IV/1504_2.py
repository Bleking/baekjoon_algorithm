# 백준 1504번 특정한 최단 경로 골드 4

import sys
import heapq

INF = int(1e9)

N, E = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]

for _ in range(E):
  a, b, c = map(int, sys.stdin.readline().split())
  graph[a].append((b, c))
  graph[b].append((a, c))

v1, v2 = map(int, sys.stdin.readline().split())

def dijkstra(node):
  heap = []
  distance = [INF] * (N+1)

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
        
  return distance

d1 = dijkstra(v1)
d2 = dijkstra(v2)

answer1 = d1[1] + d1[v2] + d2[N]
answer2 = d2[1] + d2[v1] + d1[N]

if answer1 >= INF and answer2 >= INF:
  print(-1)
else:
  print(min(answer1, answer2))
