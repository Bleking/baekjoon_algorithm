# 백준 11399번 ATM 실버 4

import sys

N = int(sys.stdin.readline())
P = list(map(int, sys.stdin.readline().split()))
P_sort = sorted(P)

temp1 = [0] * N
temp2 = [0] * N

temp1[0] = P[0]
temp2[0] = P_sort[0]
for i in range(1, N):
    temp1[i] = P[i] + temp1[i-1]
    temp2[i] = P_sort[i] + temp2[i-1]

if sum(temp1) < sum(temp2):
    print(sum(temp1))
else:
    print(sum(temp2))
