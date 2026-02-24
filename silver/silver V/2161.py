# 백준 2161번 카드1 실버 5

import sys
from collections import deque

N = int(sys.stdin.readline())
queue = deque([i for i in range(1, N+1)])

answer = []
while len(queue) > 1:
    answer.append(queue.popleft())
    queue.append(queue.popleft())

answer.append(queue.popleft())
print(*answer)
