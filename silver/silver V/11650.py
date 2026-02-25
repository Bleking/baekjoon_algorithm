# 백준 11650번 좌표 정렬하기 실버 5

import sys

N = int(sys.stdin.readline())

coordinates = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    coordinates.append((x, y))

coordinates.sort()
for c in coordinates:
    print(*c)
