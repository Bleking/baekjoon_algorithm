# 백준 10814번 나이순 정렬 실버 5

import sys

N = int(sys.stdin.readline())
people = []
for i in range(N):
    a, n = map(str, sys.stdin.readline().split())
    people.append((int(a), i, n))

people.sort()

for age, order, name in people:
    print(age, name)
