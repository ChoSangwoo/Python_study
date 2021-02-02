'''
두 정수(a, b)를 입력받아
a가 b보다 크면 1을, a가 b보다 작거나 같으면 0을 출력하는 프로그램을 작성해보자.

두 정수(a, b)를 입력받아
a와 b가 같으면 1을, 같지 않으면 0을 출력하는 프로그램을 작성해보자.

두 정수(a, b)를 입력받아
b가 a보다 크거나 같으면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.

두 정수(a, b)를 입력받아
a와 b가 서로 다르면 1을, 그렇지 않으면 0을 출력하는 프로그램을 작성해보자.
'''

a, b = map(int, input().split())
print(int(a>b))

'''
a, b = map(int, input().split())
print(int(a==b))
'''

'''
a, b = map(int, input().split())
print(int(b>=a))
'''

'''
a, b = map(int, input().split())
print(int(b!=a))
'''