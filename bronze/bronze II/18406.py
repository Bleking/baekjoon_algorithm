# 백준 18406번 럭키 스트레이트 브론즈 2

import sys

N = sys.stdin.readline().strip()

sum1 = 0
for i in range(len(N) // 2):
  sum1 += int(N[i])

sum2 =0
for j in range(len(N) // 2, len(N)):
  sum2 += int(N[j])

if sum1 == sum2:
  print('LUCKY')
else:
  print('READY')
