while True:
    ls = list(map(int, input().split()))
    if sum(ls) == 0:
        break
    ls.sort()

    if (ls[0] ** 2) + (ls[1] ** 2) == ls[2] ** 2:
        print("right")
    else:
        print("wrong")
