# 122
# 점수 구간에 해당하는 학점이 아래와 같이 정의되어 있다. 사용자로부터 score를 입력받아 학점을 출력하라.

# 점수	학점
# 81~100	A
# 61~80	B
# 41~60	C
# 21~40	D
# 0~20	E
# >> score: 83
# grade is A

score = int(input("grade is:"))
if score > 80 : 
    print("A")
elif score > 60 : 
    print("B")
elif score > 40 : 
    print("C")
elif score > 20 : 
    print("D")
elif score >= 0 :
    print("E")
