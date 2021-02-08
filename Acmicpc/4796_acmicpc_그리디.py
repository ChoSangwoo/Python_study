# 4796 캠핑 그리디
import sys
c = 0
a = []

while True:
    l, p, v = map(int ,sys.stdin.readline().split())
    if l+p+v == 0:
        break
    else:
        a.append([l, p, v])

for i in range(len(a)):
    #남은 잔여일이 연속 이용가능한 일보다 많으면 1회 최대 이용가능한날만 더해준다.
    c = ((a[i][2] // a[i][1]) * a[i][0]) + (a[i][0] if a[i][2] % a[i][1] > a[i][0] else a[i][2] % a[i][1])
    print('Case {}: {}'.format(i+1, c))