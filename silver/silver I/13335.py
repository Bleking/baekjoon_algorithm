# 백준 13335번 트럭 실버1

import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())  # 트럭 개수, 다리의 길이, 다리의 최대 무게
weights = list(map(int, sys.stdin.readline().split()))  # 트럭의 무게 리스트

def solution(num_trucks, bridge_length, weight, truck_weights):
    num_trucks = len(truck_weights)
    time = 0
    trucks = deque(truck_weights)  # 다리를 지나려고 대기중인 트럭
    bridge = deque([0] * bridge_length)
    passed = []  # 다리를 지나간 트럭 리스트

    while len(passed) < num_trucks:
        time += 1
        
        out = bridge.popleft()  # 트럭이 다리를 지나침
        if out != 0:  # 0은 빈칸을 체울 목적일 뿐이고, 존재하지 않는 트럭을 지나친 트럭 리스트에 담을 수 없음
            passed.append(out)
        
        # 2. 새 트럭 진입 (trucks가 비지 않았을 때만)
        if trucks:  # 지나갈 트럭이 있을 때만
          if sum(bridge) + trucks[0] <= weight:  # 다리의 최대 무게를 넘지 않을 경우에만
              bridge.append(trucks.popleft())  # 다음 트럭이 다리 위에 있을 수 있다.
          else:  # 현재 다리가 트럭들의 무게를 감당할 수 없는 상황이면
              bridge.append(0)  # 그 빈자리를 0으로 체운다.

    return time

print(solution(n, w, L, weights))
