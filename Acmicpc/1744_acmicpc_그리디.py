# 1744 수 묶기 그리디

n = int(input())
m = []
s = 0

for _ in range(n):
    m.append(int(input()))

m = sorted(m)

plus = []
minus = []
one = []

for i in range(len(m)):
    if m[i] < 1:
        minus.append(m[i])
    elif m[i] == 1:
        one.append(m[i])
    elif m[i] > 1:
        plus = sorted(m[i:], reverse = True)
        break

while len(plus) > 1:
    s += plus.pop(0) * plus.pop(0)
if len(plus) == 1:
    s += plus.pop(0)

while len(minus) > 1:
    s += minus.pop(0) * minus.pop(0)
if len(minus) == 1:
    s += minus.pop(0)
    
s += sum(one)
    
print(s)