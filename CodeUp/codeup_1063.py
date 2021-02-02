'''
입력된 두 정수 a, b 중 큰 값을 출력하는 프로그램을 작성해보자.
단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.

입력된 세 정수 a, b, c 중 가장 작은 값을 출력하는 프로그램을 작성해보자.
단, 조건문을 사용하지 않고 3항 연산자 ? 를 사용한다.
'''

a, b = map(int, input().split())
# [True Value] if [Condition] else [False Value]
res = a if a>b else b
print(res)

'''
a, b, c = map(int, input().split())
res1 = a if a<b else b
res2 = c if c<res1 else res1
print(res2)
'''