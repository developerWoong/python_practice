# 234
# 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.

# pickup_even([3, 4, 5, 6, 7, 8])
# [4, 6, 8]

def pickup_even(list_name):
    even_list = []
    for i in list_name:
        if  i % 2 == 0 :
            even_list.append(i)
    return even_list


    