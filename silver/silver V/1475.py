# 백준 1475번 	방 번호 실버 5

import sys

N = sys.stdin.readline().strip()

num_list = [0] * 10  # 0~9
for i in range(len(N)):
  if N[i] == '6' or N[i] == '9':
    if num_list[6] <= num_list[9]:
      num_list[6] += 1
    else:
      num_list[9] += 1
  else:
    num_list[int(N[i])] += 1

print(max(num_list))
