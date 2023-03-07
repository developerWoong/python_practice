# 269 객체의 속성 수정
# 267번에서 생성한 객체에 set_per 메서드를 호출하여 per 값을 12.75로 수정해보세요.

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

    def set_PER(self, stock_PER):
        self.stock_PER = stock_PER

    def set_PBR(self, stock_PBR):
        self.stock_PBR = stock_PBR

    def set_배당(self, stock_배당):
        self.stock_배당 = stock_배당

    def get_name(self):
        return self.stock_name

    def get_number(self):
        return self.stock_number
    
삼성전자 = Stock('삼성전자', '005930', 15.79, 1.33, 2.83)
삼성전자.set_PER(12.75)
print(삼성전자.stock_PER)

