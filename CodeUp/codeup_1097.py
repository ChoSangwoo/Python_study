'''
부모님을 기다리던 영일이는 검정/흰 색 바둑알을 바둑판에 꽉 채워 깔아 놓고 놀다가...

"십(+)자 뒤집기를 해볼까?"하고 생각했다.

바둑판(19 * 19)에 흰 돌(1) 또는 검정 돌(0)이 모두 꽉 채워져 놓여있을 때,
n개의 좌표를 입력받아 십(+)자 뒤집기한 결과를 출력하는 프로그램을 작성해보자.

'''


m = []
for i in range(19):
    pan = list(map(int, input().split()))
    m.append(pan)
    
n = int(input())

for i in range(n):
    c = list(map(int, input().split()))
    for i in range(19):
        if m[i][c[1]-1] == 1:
            m[i][c[1]-1] = 0
        else:
            m[i][c[1]-1] = 1
        if m[c[0]-1][i] == 1:
            m[c[0]-1][i] = 0
        else:
            m[c[0]-1][i] = 1
for i in m:
    for j in i:
        print(j, end=' ')
    print('')