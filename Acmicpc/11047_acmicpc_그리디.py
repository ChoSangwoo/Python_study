# 11047 동전0 그리디

n, k = map(int, input().split())
m = []
c = 0

for i in range(n):
    m.append(int(input()))
    
m = reversed(m)

for i in m:
    if k // i > 0:
        c += (k // i)
        k = k % i
    elif k // i == 0:
        continue

print(c)