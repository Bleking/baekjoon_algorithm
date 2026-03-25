# 백준 1238번 파티 골드 3

import sys
import heapq

N, M, X = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
  u, v, t = map(int, sys.stdin.readline().split())
  graph[u].append((v, t))

INF = int(1e9)

def dijkstra(start):
  heap = []
  heapq.heappush(heap, (0, start))

  distance = [INF] * (N+1)
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

  return distance

x = dijkstra(X)
answer = 0
for i in range(1, N+1):
  total = dijkstra(i)[X] + x[i]
  answer = max(answer, total)

print(answer)
