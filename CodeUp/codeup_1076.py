'''
영문자(a ~ z) 1개가 입력되었을 때 그 문자까지의 알파벳을 순서대로 출력해보자.

'q'가 입력될 때까지 입력한 문자를 계속 출력하는 프로그램을 작성해보자.
'''

n = input()

a = ord('a')
n = ord(n)

for i in range(a, n+1):
    print(chr(i))
    
'''
a = list(input().split())

for i in a:
    if i == 'q':
        print(i)
        break
    else:
        print(i)
'''