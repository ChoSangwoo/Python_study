# 1715 카드 정렬하기 그리디
import heapq
#이진트리 기반의 최소힙 자료구조 제공
#항상 정렬된 상태로 추가되며 가장 작은값의 인덱스는 0

n = int(input())
m = []
r = 0

for _ in range(n):
    heapq.heappush(m, int(input()))

if len(m) == 1:
    print(0)
else:
    while len(m) > 1:
        a = heapq.heappop(m)
        b = heapq.heappop(m)
        r += a + b
        heapq.heappush(m, a + b)
    print(r)