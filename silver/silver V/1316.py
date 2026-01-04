# 백준 1316번 그룹 단어 체커 실버5

import sys

N = int(sys.stdin.readline())  # 입력할 문자열 개수

cnt = 0
for i in range(N):
  temp = 1
  str = input()  # 문자열

  dict = {}  # 문자열의 각 문자를 key로 하고, value는 연속하는 동안 1로 유지. 그 이후에 같은 문자가 등장하면 1을 더함
  prev_c = None  # 이전 문자
  for c in str:
    if c != prev_c:  # 이전 문자와 다른 문자를 만났을 떄
      if c in dict:  # 딕셔너리에 해당 문자가 있으면
        dict[c] += 1  # 해당 문자의 key의 value에 +1
      else:  # 해당 문자가 없으면
        dict[c] = 1  # 새로 추가
      
      prev_c = c  # 다음 문자로 넘어가기 전에 현재 문자 저장. 그러다가 새로운 문자가 나오면 그것으로 교체.
    
    if dict[c] > 1:  # 특정 문자가 연속하지 않았음
      temp = 0  # 1을 더하지 않음
      break
  
  cnt += temp  # 불연속이면 0을 더함. 그렇지 않을 경우 그대로 1을 더함.

print(cnt)


# 예제
# babb => {b: 2, a:1}
# 처음에 문자 b를 만나서 b를 추가 -> 이후에 a를 만나서 a 추가 => 그 이후에 b가 한번 더 등장하여 b의 value에 +1 -> 1보다 커졌기에 거기서 거기서 프로세스를 멈춤
