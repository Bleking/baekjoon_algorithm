# 백준 11728번 배열 합치기 실 5

import sys

lenA, lenB = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

arr = A + B
arr.sort()

print(*arr)
