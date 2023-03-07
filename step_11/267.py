# 267 객체 생성
# 266번에서 정의한 생성자를 통해 다음 정보를 갖는 객체를 생성해보세요.

# 항목	정보
# 종목명	삼성전자
# 종목코드	005930
# PER	15.79
# PBR	1.33
# 배당수익률	2.83

class Stock:
    def __init__(self, stock_name, stock_number, stock_PER, stock_PBR, stock_배당):
        self.stock_name = stock_name
        self.stock_number = stock_number
        self.stock_PER = stock_PER
        self.stock_PBR = stock_PBR
        self.stock_배당 = stock_배당

    def set_name(self, stock_name):
        self.stock_name = stock_name

    def set_number(self, stock_number):
        self.stock_number = stock_number

    def get_name(self):
        return self.stock_name

    def get_number(self):
        return self.stock_number
    
삼성전자 = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
print(삼성전자.stock_name)
