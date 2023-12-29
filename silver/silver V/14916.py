import sys

n = int(sys.stdin.readline())

answer = 0
while n > 0:
  if n % 5 == 0:
    answer += (n // 5)
    break
  else:
    n -= 2
    answer += 1

if n < 0:
  answer = -1

print(answer)
