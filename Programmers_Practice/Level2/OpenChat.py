def solution(record):
    answer = []
    userDict = {}

    for mes in record:
        if (mes.split(' ')[0] == 'Enter') | (mes.split(' ')[0] == 'Change'):
            userDict[mes.split(' ')[1]] = mes.split(' ')[2]

    for mes in record:
        if mes.split(' ')[0] == 'Enter':
            # userDict[mes.split(' ')[1]] + '님이 들어왔습니다.' 이런식으로 해도 가능
            answer.append("{}님이 들어왔습니다.".format(userDict[mes.split(' ')[1]]))
        elif mes.split(' ')[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(userDict[mes.split(' ')[1]]))
        else:
            pass
    return answer
