# 277 이자 지급하기
# 입금 횟수가 5회가 될 때 잔고를 기준으로 1 % 의 이자가 잔고에 추가되도록 코드를 변경해보세요.

import random


class Account:

    account_count = 0

    def __init__(self, name, balance):
        self.deposit_count = 0

        self.name = name
        self.balance = balance
        self.bank = "SC은행"
        num1 = random.randint(0, 999)
        num2 = random.randint(0, 99)
        num3 = random.randint(0, 999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1 + '-' + num2 + '-' + num3

        Account.account_count += 1

    def get_account_num(cls):
        print(cls.account_count)

    def deposit(self, deposit):
        if deposit > 1:
            self.balance = self.balance + deposit

        self.deposit_count += 1 

        if self.deposit_count % 5 == 0:
            self.balance = (self.balance * 1.01)

    def withdraw(self, withdraw):
        if withdraw <= self.balance:
            self.balance = self.balance - withdraw

    def display_info(self):
        print('은행이름:' + self.bank)
        print('예금주:' + self.name)
        print('계좌번호:' + self.account_number)
        print('잔고:', f"{self.balance:,}")


woong = Account("박웅", 10000)
woong.deposit(10000)
woong.deposit(10000)
woong.deposit(10000)
woong.deposit(5000)
woong.deposit(5000)
print(woong.balance)

