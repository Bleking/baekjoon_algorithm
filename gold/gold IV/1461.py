# 백준 1461번 도서관 골드4

import sys

N, M = map(int, sys.stdin.readline().split())
books = list(map(int, sys.stdin.readline().split()))

negative, positive = [], []
for n in range(N):
  if books[n] < 0:
    negative.append(abs(books[n]))
  else:
    positive.append(books[n])

negative = sorted(negative, reverse=True)
positive = sorted(positive, reverse=True)

distances = []
for i in range(0, len(positive), M):
  distances.append(positive[i])
for j in range(0, len(negative), M):
  distances.append(negative[j])

distances = sorted(distances, reverse=True)

answer = distances[0]
for idx in range(1, len(distances)):
  answer += (distances[idx] * 2)

print(answer)
