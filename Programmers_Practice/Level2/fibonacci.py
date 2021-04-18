# 연습문제 - 피보나치 수열
"""
피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
* n은 1이상, 100000이하인 자연수입니다.
"""


# 첫번째 풀이 - 재귀함수를 이용했지만 효율성 하락

# def solution(n):
#     return fibonacchi(n) % (1234567)
#
#
# def fibonacchi(m):
#     if m == 0:
#         return 0
#     elif m == 1:
#         return 1
#     else:
#         return fibonacchi(m - 1) + fibonacchi(m - 2)

# 두번째 풀이 - 파이썬의 특징

def solution(num):
    a, b = 0, 1
    for i in range(num):
        a, b = b, a + b
    return a % 1234567  
