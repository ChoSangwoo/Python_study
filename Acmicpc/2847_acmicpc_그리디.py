# 2847 게임을 만든 동준이 그리디

n = int(input())
m = [int(input()) for _ in range(n)]
c = 0

for i in range(n-1, 0, -1):  
    if m[i] <= m[i-1]:
        c += (m[i-1]-m[i]+1)
        m[i-1] = m[i]-1
print(c)