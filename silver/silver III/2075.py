# 백준 2075번 N번째 큰 수 실버 3

import sys
import heapq

heap = []

N = int(sys.stdin.readline())

for _ in range(N):
  row = list(map(int, sys.stdin.readline().split()))
  for r in row:
    if len(heap) < N:
      heapq.heappush(heap, r)
    else:
      if r > heap[0]:
        # 이렇게 해도 되고
        heapq.heappop(heap)
        heapq.heappush(heap, r)
        
        # # 이렇게 해도 되고
        # heapq.heapreplace(heap, r)

print(heap[0])
