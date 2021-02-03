# 1541 잃어버린 괄호 그리디

n = input().split('-')
r = 0

for i in n[0].split('+'):
    r += int(i)

for i in n[1:]:
    for j in i.split('+'):
        r -= int(j)

print(r)