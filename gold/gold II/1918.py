# 백준 1918번 후위 표기식 골드 2

import sys

string = sys.stdin.readline().strip()

stack = []
answer = ''

for s in string:
  if s == '(':
    stack.append(s)
  elif s == ')':
    while stack[-1] != '(':  # 괄호 열기가 나올 때까지
      answer += stack.pop()  # 다른 연산자 모두 뽑아서 추가
    stack.pop()  # 마지막 '('는 추가 X
  
  elif s == '*' or s == '/':
    while stack and (stack[-1] == '*' or stack[-1] == '/'):  # 곱셈, 나눗셈이 우선 순위로 처리
      answer += stack.pop()
    stack.append(s)
  elif s == '+' or s == '-':
    while stack and (stack[-1] != '('):  # 덧셈, 뺄셈은 괄호에 둘러쌓였을 때만 우선 처리
      answer += stack.pop()
    stack.append(s)
  
  else:  # 피연산자는 그냥 추가
    answer += s

while stack:  # 그래도 스택에 뭔가 남아있으면
  answer += stack.pop()  # 모두 다 뽑아서 넣자

print(answer)
