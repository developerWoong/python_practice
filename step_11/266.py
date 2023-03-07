# 266 객체의 속성값 업데이트
# 생성자에서 종목명, 종목코드, PER, PBR, 배당수익률을 입력 받을 수 있도록 생성자를 수정하세요. PER, PBR, 배당수익률은 float 타입입니다.

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
