# 백준 10825번 국영수 실버 4

import sys

N = int(sys.stdin.readline())

students = []
for i in range(N):
    name, kor, eng, math = sys.stdin.readline().strip().split()  # 학생 이름, 국, 영, 수
    students.append([name, int(kor), int(eng), int(math)])

students.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in range(N):
    print(students[i][0])
