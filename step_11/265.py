# 265 메서드
# 종목명과 종목코드를 리턴하는 get_name, get_code 메서드를 추가하세요. 해당 메서드를 사용하여 종목명과 종목코드를 얻고 이를 출력해보세요.
# 삼성 = Stock("삼성전자", "005930")

class Stock:
    def __init__(self, stock_name, stock_number):
        self.stock_name = stock_name
        self.stock_number = stock_number

    def set_name(self, stock_name):
        self.stock_name = stock_name

    def set_number(self, stock_number):
        self.stock_number = stock_number

    def get_name(self):
        return self.stock_name
       
    def get_number(self):
        return self.stock_number
    

삼성 = Stock("삼성전자", "005930")
print(삼성.stock_name)
print(삼성.stock_number)
print(삼성.get_name())
print(삼성.get_number())

    