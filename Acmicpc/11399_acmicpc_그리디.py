# 11399 ATM 그리디

n = int(input())
p = list(map(int, input().split()))
m = 0
p.sort()

for i in range(len(p)):
    for j in range(i+1):
        m += p[j]
        
print(m)