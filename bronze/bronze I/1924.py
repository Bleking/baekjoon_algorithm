# 백준 1924번 2007 브론즈 1

import sys

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

x, y = map(int, sys.stdin.readline().split())

total_days = sum(month[:x]) + y - 1

print(week[total_days % 7])
