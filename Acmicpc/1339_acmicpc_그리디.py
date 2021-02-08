# 1339 단어수학 그리디
import sys

n = int(sys.stdin.readline())
a = []
for _ in range(n):
    a.append(list(sys.stdin.readline().rstrip()))

d = {}
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] not in d:
            d[a[i][j]] = pow(10, len(a[i])-j-1)
        else:
            d[a[i][j]] += pow(10, len(a[i])-j-1)
    
s = sorted(d.items(), key=lambda x: x[1], reverse=True)
r, num = 0, 9

for i in range(len(s)):
    r += num * s[i][1]
    num -= 1

print(r)