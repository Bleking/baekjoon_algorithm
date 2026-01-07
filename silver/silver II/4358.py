# 백준 4358번 생태 실버2

import sys

tree_list = {}

cnt = 0
while True:
  tree = sys.stdin.readline().rstrip()

  if tree == '':
    break
  cnt += 1
  if tree not in tree_list:
    tree_list[tree] = 0
  tree_list[tree] += 1

for idx in sorted(tree_list.keys()):
  print("%s %.4f" % (idx, tree_list[idx] / cnt * 100))
