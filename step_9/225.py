# 225
# my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.

# my_dict = {"10/26": [100, 130, 100, 100],
#            "10/27": [10, 12, 10, 11]}
# my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.

# print_value_by_key(my_dict, "10/26")
# [100, 130, 100, 100]

my_dict = {"10/26": [100, 130, 100, 100],
           "10/27": [10, 12, 10, 11]}

def print_value_by_key(dic, keys):
    print(dic[keys])
