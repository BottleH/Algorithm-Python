"""
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
"""
# 해당 문제는 메모리 제한이 매우 크다..

import sys

N = int(sys.stdin.readline())
result = [0] * 10001

for i in range(N):
    num = int(sys.stdin.readline())
    result[num] += 1

for i in range(len(result)):
    for j in range(result[i]):
        print(i)
