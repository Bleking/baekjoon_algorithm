# 백준 1766번 문제 골드 2

import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)

for _ in range(M):
  a, b = map(int, sys.stdin.readline().split())

  graph[a].append(b)
  in_degree[b] += 1

def topology_sort():
  heap = []

  for i in range(1, N+1):
    if in_degree[i] == 0:
      heapq.heappush(heap, i)

  answer = []
  while heap:
    now = heapq.heappop(heap)

    answer.append(now)
    for next in graph[now]:
      in_degree[next] -= 1

      if in_degree[next] == 0:
        heapq.heappush(heap, next)
        
  return answer

print(*topology_sort())
