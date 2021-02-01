'''
정수(int) 2개를 입력받아 그대로 출력해보자.
'''

#split()이용하여 input할 경우에 list자료형이 됨
#map()이용하여 int형변환
a,b = map(int, input().split())
print(a,b)