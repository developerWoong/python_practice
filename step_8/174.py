# 174
# 아래와 같이 리스트의 데이터를 출력하라. 단, for문과 range문을 사용하라.

# price_list = [32100, 32150, 32000, 32500]
# 100 32150
# 110 32000
# 120 32500

price_list = [32100, 32150, 32000, 32500]

for i in range(3):
    print(100 + (10 * i), price_list[i + 1])

# 다른 답안: 
# for i in range(1, 4):
#     print(90 + 10 * i, price_list[i])
