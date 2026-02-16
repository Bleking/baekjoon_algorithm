# 백준 1026번 보 실버 4

import sys

N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()
B.sort(reverse=True)

answer = 0
for i in range(N):
    answer += (A[i] * B[i])
