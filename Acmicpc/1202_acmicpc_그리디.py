# 1202 보석 도둑 그리디
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())

a = []
b = []
c = 0

for _ in range(n):
    heapq.heappush(a, list(map(int, sys.stdin.readline().split())))
for _ in range(k):
    b.append(int(sys.stdin.readline()))
b.sort()

#가방에 들어갈 수 있는 보석들중에 제일 비싼거만 넣자
#보석 무게 오름차순 가방 무게 오름차순
tmp = []
for i in b:
    while a and i >= a[0][0]:
        heapq.heappush(tmp, -heapq.heappop(a)[1])
    if tmp:
        c -= heapq.heappop(tmp)
    elif not a:
        break
print(c)