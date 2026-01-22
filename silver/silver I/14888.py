# 백준 14888번 연산자 끼워넣기 실버1

import sys
from itertools import permutations

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
computation_num = list(map(int, sys.stdin.readline().split()))  # 덧셈(+) 개수, 뺄셈(-) 개수, 곱셈(×) 개수, 나눗셈(÷) 개수

computations = []
computations += ['+'] * computation_num[0]
computations += ['-'] * computation_num[1]
computations += ['*'] * computation_num[2]
computations += ['/'] * computation_num[3]

comp_perm = permutations(computations, N-1)
answer = []
for comp in comp_perm:
  res = nums[0]
  for i in range(N-1):
    if comp[i] == '+':
      res += nums[i+1]
    elif comp[i] == '-':
      res -= nums[i+1]
    elif comp[i] == '*':
      res *= nums[i+1]
    elif comp[i] == '/':
      if res < 0:
          res = -(-res // nums[i+1])  # -(7//3) = -2
      else:
          res = res // nums[i+1]
  answer.append(res)

print(max(answer))
print(min(answer))
