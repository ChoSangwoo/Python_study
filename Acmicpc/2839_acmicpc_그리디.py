# 2839 설탕 배달 그리디

n = int(input())
c = 0

while True:
    if n % 5 != 0:
        if n == 1 or n == 2:
            c = -1
            break
        else:
            n -= 3
            c += 1
    elif n % 5 == 0:        
        c += (n // 5)
        break

print(c)