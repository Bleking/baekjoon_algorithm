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

def dijkstra(start, end):
  heap = []
  distance = [INF] * (N+1)

  heapq.heappush(heap, (0, start))
  distance[start] = 0

  while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
      continue

    for g in graph[now]:
      cost = dist + g[1]

      if cost < distance[g[0]]:
        distance[g[0]] = cost
        heapq.heappush(heap, (cost, g[0]))
  
  return distance[end]

ans1 = dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N)
ans2 = dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N)

if ans1 >= INF and ans2 >= INF:
  print(-1)
else:
  print(min(ans1, ans2))
