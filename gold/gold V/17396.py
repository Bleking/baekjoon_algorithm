# 백준 17396번 백도 골드 5

import sys
import heapq

INF = int(1e18)

N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))  # a[0]=0, a[N-1]=1

graph = [[] for _ in range(N)]
for _ in range(M):
  a, b, t = map(int, sys.stdin.readline().split())
  graph[a].append((b, t))
  graph[b].append((a, t))

distance = [INF] * N

def dijkstra(start, end):
  heap = []

  heapq.heappush(heap, (0, start))
  distance[start] = 0

  while heap:
    dist, now = heapq.heappop(heap)

    if distance[now] < dist:
      continue
    
    if A[now] == 1 and now != 0 and now != N-1:  # 시작과 끝을 제외하고 현재 노드가 시야 노드면 피하기
      continue

    for g in graph[now]:
       cost = dist + g[1]

       if cost < distance[g[0]] and (A[g[0]] == 0 or g[0] == N-1):  # 이 부분이 중요!
        distance[g[0]] = cost
        heapq.heappush(heap, (cost, g[0]))
        
  return distance[end]

answer = dijkstra(0, N-1)
if answer == INF:
  print(-1)
else:
  print(answer)  # 시작점과 끝점을 선언만 하면 거기까지 주욱 내려간다.
