# 1946 신입사원 그리디
import sys

#input()으로 하면 시간초과
#sys 라이브러리의 readline() 활용
t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    m = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(n)], key = lambda a:a[0])
    
    min_p = m[0][1]
    c = 0
    for i in range(1, n):
        if m[i][1] < min_p:
            c += 1
            min_p = m[i][1]
    
    print(c+1)