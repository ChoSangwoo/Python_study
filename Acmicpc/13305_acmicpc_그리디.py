# 13305 주유소 그리디

n = input().split()
l = list(map(int, input().split()))
p = list(map(int, input().split()))
r = 0

sum_l = 0
min_p = p[0]
 
#처음 시작할때는 왼쪽에서 채우고 시작
#지금 도시보다 더 싼 가격의 도시가 나올때까지 찾으면
#거기까지는 지금 도시의 기름값으로 더 싼 도시까지의 거리만큼 주유
for i in range(len(p)-1):
    if p[i] < min_p:
        min_p = p[i]
    r += min_p * l[i]
       
print(r)