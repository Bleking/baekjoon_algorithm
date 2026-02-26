# 백준 1269번 대칭 차집합 실 4

import sys

num_A, num_B = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A = set(A)
B = set(B)

print(len(A-B) + len(B-A))
