import sys

N = int(sys.stdin.readline())
num_list = list(map(int, sys.stdin.readline().split()))

dp1 = [1] * N
dp2 = [1] * N

# 연속해서 커질 때
for i in range(N-1):
  if num_list[i] <= num_list[i+1]:
    dp1[i+1] += dp1[i]

# 연속해서 작아질 때
for i in range(N-1):
  if num_list[i] >= num_list[i+1]:
    dp2[i+1] += dp2[i]

print(max(max(dp1), max(dp2)))
