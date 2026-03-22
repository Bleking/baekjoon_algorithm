# 백준 2252번 줄 세우기 골드 3

import sys
import heapq

N, M = map(int, sys.stdin.readline().split())  # 노드, 엣지 개수

in_degree = [0] * (N+1)  # 모든 노드에 대한 진입차수는 0으로 초기화

graph = [[] for _ in range(N+1)]  # 각 노드에 대한 연결 정보를 위한 연결 리스트

for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())

  graph[u].append(v)  # 노드 u에서 v로 연결
  in_degree[v] += 1  # 노드 v로 향하는 진입 차수 1 증가

def topology_sort():
  heap = []
  # 처음에는 진입차수가 0인 노드를 큐에 삽입
  for i in range(1, N+1):
    if in_degree[i] == 0:
      heapq.heappush(heap, i)

  answer = []
  while heap:
    now = heapq.heappop(heap)
    answer.append(now)

    # 현재 노드와 연결된 노드들의 진입차수에서 1 빼기
    for next in graph[now]:
      in_degree[next] -= 1

      # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
      if in_degree[next] == 0:
        heapq.heappush(heap, next)

  return answer

print(*topology_sort())
