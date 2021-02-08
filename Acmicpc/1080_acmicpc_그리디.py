# 1080 행렬 그리디

n, m = map(int ,input().split())
a = [list(map(int, list(input()))) for _ in range(n)]
b = [list(map(int, list(input()))) for _ in range(n)]
c = 0

def op(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            a[i][j] = 1 - a[i][j]

for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != b[i][j]:
            op(i, j)
            c += 1

if a != b:
    c = -1
    
print(c)