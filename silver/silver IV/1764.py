# 백준 1764번 듣보잡 실버 4

import sys

N, M = map(int, sys.stdin.readline().split())

d, b = set(), set()
for _ in range(N):
    d.add(sys.stdin.readline().strip())
for _ in range(M):
    b.add(sys.stdin.readline().strip())

db = list(d & b)
db = sorted(db)

print(len(db))
for name in db:
    print(name)
