# 백준 2252번 줄 세우기 골드 3

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N+1)]
in_degree = [0] * (N+1)  # 진입차수: 각 노드마다 가리키는 화살표의 개수

for _ in range(M):
  u, v = map(int, sys.stdin.readline().split())
  graph[u].append(v)  # u -> v
  in_degree[v] += 1  # 노드 v의 진입차수 +1

def topology_sort():
  queue = deque()

  # 진입차수가 0인 노드 모두 추가
  for i in range(1, N+1):
    if in_degree[i] == 0:
      queue.append(i)

  answer = []
  while queue:
    now = queue.popleft()
    answer.append(now)  # 순서 기록

    for g in graph[now]:
      in_degree[g] -= 1  # 화살표 제거

      if in_degree[g] == 0:  # g 노드로 향하는 화살표가 없으면
        queue.append(g)  # 그것을 큐에 추가

  return answer

print(*topology_sort())
