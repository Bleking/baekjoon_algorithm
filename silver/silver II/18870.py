# 백준 18870번 좌표 압축 실버 2

import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().split()))

X_set = sorted(set(X))
X_dict = {}
for idx in range(len(X_set)):
    X_dict[X_set[idx]] = idx

answer = []
for x in X:
    answer.append(X_dict[x])

print(*answer)
