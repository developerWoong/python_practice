# 154
# 리스트에서 세 글자 이상의 문자를 화면에 출력하라

# 리스트 = ["I", "study", "python", "language", "!"]
# study
# python
# language

리스트 = ["I", "study", "python", "language", "!"]

for 문자 in 리스트:
    if len(문자) >= 3:
        print(문자)