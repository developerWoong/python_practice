# 295 파일 읽기
# 바탕화면에 생성한 '매수종목2.txt' 파일을 읽은 후 종목코드와 종목명을 딕셔너리로 저장해보세요. 종목명을 key로 종목명을 value로 저장합니다.

# 005930 삼성전자
# 005380 현대차
# 035420 NAVER

f = open("/users/parkwoong/Desktop/매수종목2.txt", encoding="utf-8")
lines = f.readlines()

data = {}
for line in lines:
    line = line.strip()
    k, v = line.split()

    data[k] = v

print(data)
f.close()