# 119
# 아래와 같이 fruit 딕셔너리가 정의되어 있다. 사용자가 입력한 값이 딕셔너리 키(key) 값에 포함되었다면 "정답입니다"를 아닐 경우 "오답입니다" 출력하라.

# fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}
# >> 제가좋아하는계절은: 봄
# 정답입니다.

fruit = {"봄": "딸기", "여름": "토마토", "가을": "사과"}

season = input("제가 좋아하는 계절은:")
if season in fruit:
    print("정답입니다.")
else : 
    print("오답입니다.")
