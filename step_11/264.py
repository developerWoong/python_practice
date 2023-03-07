# 264 메서드
# 객체에 종목코드를 입력할 수 있는 set_code 메서드를 추가해보세요.

# a = Stock(None, None)
# a.set_code("005930")

class Stock:
    def __init__(self, stock_name, stock_number):
        self.stock_name = stock_name
        self.stock_number = stock_number

    def set_name(self, stock_name):
        self.stock_name = stock_name

    def set_number(self, stock_number):
        self.stock_number = stock_number

a = Stock(None, None)
a.set_number("005930")
print(a.stock_number)
        