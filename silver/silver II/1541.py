# 백준 1541번 잃어버린 괄호 실버2

import sys

num_string = sys.stdin.readline()

num_list1 = num_string.split('-')  # 우선 -로 분리

result = []
for i in num_list1:
    num_list2 = list(map(int, i.split('+')))  # 그 다음에 +로 분리
    result.append(sum(num_list2))

print(result[0] - sum(result[1:]))  # 첫 번째 합에서 나머지 합을 모두 빼면 식의 값을 최소로 할 수 있다.
