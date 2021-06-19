ls_a = []
ls_b = []
ans_a = 0
ans_b = 0

for _ in range(3):
    a, b = map(int, input().split())
    ls_a.append(a)
    ls_b.append(b)
    
for i in range(3):
    if ls_a.count(ls_a[i]) == 1:
        ans_a = ls_a[i]
    if ls_b.count(ls_b[i]) == 1:
        ans_b = ls_b[i]
print(ans_a, ans_b)
