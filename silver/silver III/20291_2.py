# 백준 20291번 파일 정리 실버 3

import sys

N = int(sys.stdin.readline())

files = {}
for i in range(N):
  f = sys.stdin.readline().strip()
  file_format = f.split('.')[1]

  if file_format not in files:
    files[file_format] = 0
  files[file_format] += 1

f_list = list(files.items())
f_list = sorted(f_list, key=lambda x: x[0])

for x, y in f_list:
  print(x, y)
