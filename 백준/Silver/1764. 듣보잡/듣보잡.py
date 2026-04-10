import sys

N, M = map(int, sys.stdin.readline().split())

d, b = [], []
for _ in range(N):
    d.append(sys.stdin.readline().strip())
for _ in range(M):
    b.append(sys.stdin.readline().strip())

d, b = set(d), set(b)
db = d & b

db = list(db)
db.sort()

print(len(db))
for i in db:
    print(i)