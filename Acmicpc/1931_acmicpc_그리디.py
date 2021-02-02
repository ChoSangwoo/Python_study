# 1931 동전0 그리디

n = int(input())
m = []
cnt = 0
end = 0

for i in range(n):
    t = list(map(int, input().split()))
    m.append(t)

'''
끝나는 시간이 빠른 순서대로 정렬하되
시작시간과 끝나는시간이 같은경우를 구분하기 위해서
정렬을 두번한다.
'''
m.sort(key=lambda a:(a[1], a[0]))

for i, j in m:
    if i >= end:
        end = j
        cnt += 1
        
print(cnt)