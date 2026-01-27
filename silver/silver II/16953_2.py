# 백준 16953번 A → B 실버 2 (BFS 사용)

import sys
from collections import deque

def BFS(A, B):
  queue = deque()
  queue.append((A, 1))

  while queue:
    now, count = queue.popleft()

    if now * 2 <= B:
      queue.append((now * 2, count + 1))
    if now*10 + 1 <= B:
      queue.append((now * 10 + 1, count + 1))

    if now == B:
      return count

  return -1

A, B = map(int, sys.stdin.readline().split())
print(BFS(A, B))
