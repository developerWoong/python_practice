# 268 객체의 속성 수정
# PER, PBR, 배당수익률은 변경될 수 있는 값입니다. 이 값을 변경할 때 사용하는 set_per, set_pbr, set_dividend 메서드를 추가하세요.

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
