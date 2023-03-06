# 233
# 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.

# make_list("abcd")
# ['a', 'b', 'c', 'd']

def make_list(string):
    my_list = []
    for 변수 in string:
        my_list.append(변수)
    return my_list

# 다른 답안:
# def make_list(string):
#     return list(string)