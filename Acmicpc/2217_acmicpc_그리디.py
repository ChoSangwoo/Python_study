# 2217 로프 그리디

n = int(input())
m = []
for i in range(n):
    a = int(input())
    m.append(a)

m.sort(reverse=True)

#로프를 더했을때, 마지막 더한 로프 * 병렬로 연결한 수 가
#로프를 더하기 전에 매달 수 있는 중량보다 낮아지면 끝
for i in range(len(m)):  
    m[i] = m[i] * (i+1)  
        
print(max(m))