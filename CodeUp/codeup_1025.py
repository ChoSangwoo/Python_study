'''
다섯 자리의 정수 1개를 입력받아 각 자리별로 나누어 출력한다.
'''

a = input()
c = 4
for i in a:
    res = i+'0'*c
    print('[''{}'']'.format(res))
    c -= 1