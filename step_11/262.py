# 262 생성자
# Stock 클래스의 객체가 생성될 때 종목명과 종목코드를 입력 받을 수 있도록 생성자를 정의해보세요.

# 삼성 = Stock("삼성전자", "005930")

class Stock:
    def __init__(self, stock_name, stock_number):
        self.stock_name = stock_name
        self.stock_number = stock_number


삼성 = Stock("삼성전자", "005930")
print(삼성.stock_name)
print(삼성.stock_name)
