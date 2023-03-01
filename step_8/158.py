# 158
# 파일 이름이 저장된 리스트에서 확장자를 제거하고 파일 이름만 화면에 출력하라. (힌트: split() 메서드)

# 리스트 = ['hello.py', 'ex01.py', 'intro.hwp']
# hello
# ex01
# intro

리스트 = ['hello.py', 'ex01.py', 'intro.hwp']

for 변수 in 리스트:
    변수_이름 = 변수.split(".")
    print(변수_이름[0])
