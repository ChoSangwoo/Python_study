# 2437 저울 그리디

n = int(input())
s = list(map(int, input().split()))
s.sort()
num = 1
for i in s:
    if num < i:
        break
    else:
        num += i
print(num)