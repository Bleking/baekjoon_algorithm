# 백준 2470번 최대 힙 실버 2

import heapq
import sys

N = int(sys.stdin.readline())

heap = []
for n in range(N):
    x = int(sys.stdin.readline())
    if x == 0:
        if not heap:
            print(0)
        else:
            print(-heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)
