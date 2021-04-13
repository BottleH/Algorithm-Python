# 스택/큐 - 주식가격
"""
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution
함수를 완성하세요.
"""


# 내가 푼 첫 번째 풀이 - Stack or Que 사용 X
def solution(prices):
    answer = []

    for i in range(len(prices) - 1):
        temp = 0
        for j in range(i + 1, len(prices)):
            temp += 1
            if prices[i] > prices[j]:
                break
        answer.append(temp)
    answer.append(0)

    return answer
