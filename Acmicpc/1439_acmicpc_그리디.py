# 1439 뒤집기 그리디
import re, sys

#정규표현식 패턴매칭
pattern_1 = r"1+"
pattern_2 = r"0+"
text = sys.stdin.readline()
# 매칭된 값은 리스트로 모두 반환
m1 = re.findall(pattern_1,text)
m2 = re.findall(pattern_2,text)

m3 = min(len(m1), len(m2))

print(m3)

