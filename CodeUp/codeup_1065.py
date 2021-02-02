'''
세 정수 a, b, c가 입력되었을 때, 짝수만 출력해보자.

정수 1개가 입력되었을 때, 음(minus)/양(plus)과 짝(even)/홀(odd)을 출력해보자.
'''

a, b, c = map(int, input().split())

if a % 2 == 0:
    print(a)
    
if b % 2 == 0:
    print(b)
    
if c % 2 == 0:
    print(c)

'''
a = int(input())

if a > 0:
    print('plus')
else:
    print('minus')

if a % 2 == 0:
    print('even')
else:
    print('odd')
'''