# 177
# 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하라.

# my_list = ["가", "나", "다", "라"]
# 라 다
# 다 나
# 나 가

my_list = ["가", "나", "다", "라"]

for i in range(1, len(my_list)):
    print(my_list[len(my_list) - i], my_list[len(my_list) - (i+1)])

# 다른 답안:
# for i in range(len(my_list) - 1):
#     print(my_list[len(my_list) - 1 - i], my_list[len(my_list) - 2 - i])
