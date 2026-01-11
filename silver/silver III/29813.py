# 백준 29813 최애의 팀원 실버3

import sys
from collections import deque

N = int(sys.stdin.readline())

students = deque()

for _ in range(N):
  initial, num = input().split()
  students.append((initial, int(num)))

while len(students) > 1:
  first = students.popleft()
  
  for i in range(first[1] - 1):
    students.append(students.popleft())
  students.popleft()

print(students[0][0])
