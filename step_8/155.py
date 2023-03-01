# 155
# 리스트에서 대문자만 화면에 출력하라.

# 리스트 = ["A", "b", "c", "D"]
# A
# D

리스트 = ["A", "b", "c", "D"]

for 변수 in 리스트:
    if 변수.islower() == False:
        print(변수)

# 다른 답안:
# 리스트 = ["A", "b", "c", "D"]
# for 변수 in 리스트:
#   if 변수.isupper():
#     print(변수)
