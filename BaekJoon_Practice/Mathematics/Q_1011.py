T = int(input())

for _ in range(T):
    x, y = map(int, input().split())


def dist(x, y):
    distance = 0
    cnt = 0
    while distance != y:
        if x == 0:
            distance = 1
            cnt = 1
        else:
            distance = 3 * distance

    print(cnt)
