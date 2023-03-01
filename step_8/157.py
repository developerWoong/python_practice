# 157
# 이름의 첫 글자를 대문자로 변경해서 출력하라.

# 리스트 = ['dog', 'cat', 'parrot']
# Dog
# Cat
# Parrot
# (참고) upper() 메서드는 문자열을 대문자로 변경합니다.

# >> 변수 = "a"
# >> a.upper()
# A
# >> 변수 = "abc"
# >> 변수.upper()
# ABC

리스트 = ['dog', 'cat', 'parrot']

for 변수 in 리스트:
    print(변수[0].upper() + 변수[1:])

# 다른 답안:
# 리스트 = ['dog', 'cat', 'parrot']
# for 변수 in 리스트:
#   첫글자 = 변수[0]
#   대문자 = 첫글자.upper()     
#   print(대문자 + 변수[1:])     
