# 263 메서드
# 객체에 종목명을 입력할 수 있는 set_name 메서드를 추가해보세요.

# a = Stock(None, None)
# a.set_name("삼성전자")

class Stock:
    def __init__(self, stock_name, stock_number):
        self.stock_name = stock_name
        self.stock_number = stock_number
        
    def set_name(self, stock_name):
        self.stock_name = stock_name


a = Stock(None, None)
a.set_name("삼성전자")
print(a.stock_name)
