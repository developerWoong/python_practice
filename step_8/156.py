# 156
# 리스트에서 소문자만 화면에 출력하라.

# 리스트 = ["A", "b", "c", "D"]
# b
# c

리스트 = ["A", "b", "c", "D"]

for 변수 in 리스트:
    if 변수.islower() == True:
        print(변수)

# 다른 답안:
# 리스트 = ["A", "b", "c", "D"]
# for 변수 in 리스트:
#   if 변수.isupper() == False:
#     print(변수)
