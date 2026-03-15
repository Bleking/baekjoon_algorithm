# 백준 12891번 DNA 비밀번호 실버 2

import sys

S, P = map(int, input().split())
dna = list(input())
a, c, g, t = map(int, input().split())

answer = 0
start, end = 0, P
sliding_window = dna[start:end]

acgt_dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for i in range(P):
  if sliding_window[i] == 'A':
    acgt_dict['A'] += 1
  elif sliding_window[i] == 'C':
    acgt_dict['C'] += 1
  elif sliding_window[i] == 'G':
    acgt_dict['G'] += 1
  elif sliding_window[i] == 'T':
    acgt_dict['T'] += 1

if acgt_dict['A'] >= a and acgt_dict['C'] >= c and acgt_dict['G'] >= g and acgt_dict['T'] >= t:
  answer += 1

for i in range(S-P):  # DNA 문자열 크기를 넘어가지 않도록
  # 제외된 문자
  if dna[i] == 'A':
    acgt_dict['A'] -= 1
  elif dna[i] == 'C':
    acgt_dict['C'] -= 1
  elif dna[i] == 'G':
    acgt_dict['G'] -= 1
  elif dna[i] == 'T':
    acgt_dict['T'] -= 1
  
  # 추가된 문자
  if dna[i+P] == 'A':
    acgt_dict['A'] += 1
  elif dna[i+P] == 'C':
    acgt_dict['C'] += 1
  elif dna[i+P] == 'G':
    acgt_dict['G'] += 1
  elif dna[i+P] == 'T':
    acgt_dict['T'] += 1

  # 확인하기
  if acgt_dict['A'] >= a and acgt_dict['C'] >= c and acgt_dict['G'] >= g and acgt_dict['T'] >= t:
    answer += 1

print(answer)
