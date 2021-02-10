# 1783 병든 나이트 그리디

n, m = map(int, input().split())
c = 0

if n == 1:
    c = 1
elif n == 2:
    c = min(4, (m+1)//2)
else:
    if m < 7:
        c = min(4, m)
    else:
        c = m-2

print(c)