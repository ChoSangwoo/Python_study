# 1449 수리공 항승 그리디

n, l = map(int, input().split())
m = list(map(int, input().split()))

m.sort()
s = m[0]
e = m[0] + l
c = 1
for i in range(n):
    if s <= m[i] and m[i] < e:
        continue
    else:
        s = m[i]
        e = m[i] + l
        c += 1
print(c)