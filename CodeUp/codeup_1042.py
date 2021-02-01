'''
정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.
단, -2147483648 <= a <= b <= +2147483647, b는 0이 아니다.

정수 2개(a, b) 를 입력받아 a를 b로 나눈 나머지를 출력해보자.
단, 0 <= a, b <= +2147483647, b는 0이 아니다.
'''

a, b = map(int, input().split())
c = a//b
print(c)

'''
a, b = map(int, input().split())
c = a%b
print(c)
'''