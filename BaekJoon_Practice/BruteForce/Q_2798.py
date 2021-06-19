from itertools import combinations

n, m = map(int, input().split())
card = list(map(int, input().split()))
max_num = 0

for i in combinations(card, 3):
    if max_num < sum(i) <= m:
        max_num = sum(i)
print(max_num)
