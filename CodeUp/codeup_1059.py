'''
입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)

입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)
IP class 판단에 사용

두가지 정수의 or과 xor연산은 그래픽처리에 주로 사용
'''

a = int(input())
print(~a)

'''
a, b = map(int, input().split())
print(a & b)
'''
