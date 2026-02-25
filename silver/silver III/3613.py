# 백준 3613번 Java vs C++ 실버 3

import sys

S = sys.stdin.readline().strip()

if S[0].isupper() or S[0] == '_' or S[-1] == '_':  # 첫/끝 문자 체크
    print("Error!")
elif '_' in S and any(c.isupper() for c in S):  # 둘 다 섞임
    print("Error!")
elif '__' in S:  # 연속 언더스코어
    print("Error!")

# C++ -> Java
elif '_' in S:
  cpp = S.split('_')

  for i in range(1, len(cpp)):
    cpp[i] = cpp[i][0].upper() + cpp[i][1:]
  print(''.join(cpp))

# Java -> C++
elif '_' not in S:
  java = ''
  for i in range(len(S)):
    if S[i].isupper():
      java += ('_' + S[i].lower())
    else:
      java += S[i]
      
  print(java)
