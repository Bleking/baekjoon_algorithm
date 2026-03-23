# 백준 1005번 ACM Craft 골드 3

import sys
from collections import deque

def topology_sort():
  queue = deque()

  for i in range(1, N+1):
    if in_degree[i] == 0:
      queue.append(i)

  answer = [0] * (N+1)
  while queue:
    now = queue.popleft()

    answer[now] += D[now]
    for next in graph[now]:
      in_degree[next] -= 1

      answer[next] = max(answer[next], answer[now])
      if in_degree[next] == 0:
        queue.append(next)

  return answer

T = int(sys.stdin.readline())

for t in range(T):
  N, K = map(int, sys.stdin.readline().split())  # 건물 개수, 건물간 건설순서 규칙의 총 개수
  D = [0] + list(map(int, sys.stdin.readline().split()))  # 건물 당 걸리는 시간

  in_degree = [0] * (N+1)
  graph = [[] for _ in range(N+1)]

  for _ in range(K):
    x, y = map(int, sys.stdin.readline().split())

    graph[x].append(y)
    in_degree[y] += 1

  W = int(sys.stdin.readline())  # 승리하기 위해 건설해야 할 건물 번호

  print(topology_sort()[W])
