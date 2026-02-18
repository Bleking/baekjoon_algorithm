# 백준 15720번	카우버거 실버 5

import sys
from collections import deque

B, C, D = map(int, sys.stdin.readline().split())
burgers = list(map(int, sys.stdin.readline().split()))
sides = list(map(int, sys.stdin.readline().split()))
drinks = list(map(int, sys.stdin.readline().split()))

burgers.sort(reverse=True)
sides.sort(reverse=True)
drinks.sort(reverse=True)

burgers = deque(burgers)
sides = deque(sides)
drinks = deque(drinks)

price1 = sum(burgers) + sum(sides) + sum(drinks)

N = max(B, C, D)  # 3
M = min(B, C, D)  # 2

total = 0
for i in range(M):
    total += ((burgers.popleft() + sides.popleft() + drinks.popleft()) * 0.9)

print(price1)

total += (sum(burgers) + sum(sides) + sum(drinks))
print(int(total))
