# 백준 20186번 수 고르기 실버 4

import sys

N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))

num_list.sort(reverse=True)

answer = 0
for i in range(K):
    answer += (num_list[i] - i)

print(answer)
