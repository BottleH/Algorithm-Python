def solution(num):
    answer = str(num + 1)

    answer = answer.replace("0", "1")

    return answer


num = 9949999
ret = solution(num)

print("solution 함수의 반환 값은", ret, "입니다.")
