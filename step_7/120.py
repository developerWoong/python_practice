# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 값(value)에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# >> 좋아하는과일은? 한라봉
# 오답입니다.

fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

favorite_fruit = input("좋아하는 과일은?")
if favorite_fruit in fruit.values():
    print("정답입니다.")
else :
    print("오답입니다.")
