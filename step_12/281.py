# 281 클래스 정의
# 다음 코드가 동작하도록 차 클래스를 정의하세요.

# >> car = 차(2, 1000)
# >> car.바퀴
# 2
# >> car.가격
# 1000

class 차:
    def __init__(self, 바퀴, 가격):
        self.바퀴 = 바퀴
        self.가격 = 가격

car = 차(2, 1000)
print(car.바퀴)
print(car.가격)