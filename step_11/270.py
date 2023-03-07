# 270 여러 종목의 객체 생성
# 아래의 표를 참조하여 3종목에 대해 객체를 생성하고 이를 파이썬 리스트에 저장하세요. 파이썬 리스트에 저장된 각 종목에 대해 for 루프를 통해 종목코드와 PER을 출력해보세요.

# 종목명	종목코드	PER	PBR	배당수익률
# 삼성전자	005930	15.79	1.33	2.83
# 현대차	005380	8.70	0.35	4.27
# LG전자	066570	317.34	0.69	1.37

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
    
삼성전자 = Stock("삼성전자", '005930', 15.79, 1.33 ,2.83)
현대차 = Stock("현대차", '005380', 8.70, 0.35 ,4.27)
LG전자 = Stock("LG전자", '066570', 317.34,0.69 ,1.37)

for i in [삼성전자, 현대차, LG전자]:
    print(i.stock_number)
    print(i.stock_PER)

