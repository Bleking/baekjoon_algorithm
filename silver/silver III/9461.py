# 백준 9461번 파도반 수열 실버 3

import sys

P = [0, 1, 1, 1, 2, 2]

for i in range(6, 101):
    P.append(P[i-1] + P[i-5])

T = int(sys.stdin.readline())
for _ in range(T):
    N = int(sys.stdin.readline())
    print(P[N])
