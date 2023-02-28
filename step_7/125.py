# 125
# 휴대폰 번호 앞자리에 따라 통신사는 아래와 같이 구분된다. 사용자로부터 휴대전화 번호를 입력 받고, 통신사를 출력하는 프로그램을 작성하라.

# 번호	통신사
# 011	SKT
# 016	KT
# 019	LGU
# 010	알수없음
# >> 휴대전화 번호 입력: 011-345-1922
# 당신은 SKT 사용자입니다.

number = input("휴대전화 번호 입력:").split("-")
if number[0] == "011" :
    print("당신은 SKT 사용자입니다.")
elif number[0] == "016":
    print("당신은 KT 사용자입니다.")
elif number[0] == "019":
    print("당신은 LGU 사용자입니다.")
elif number[0] == "010":
    print("당신은 알수없음 사용자입니다.")

# 다른 답변:
# number = input("휴대전화 번호 입력: ")
# num = number.split("-")[0]
# if num == "011":
#     com = "SKT"
# elif num == "016":
#     com = "KT"
# elif num == "019":
#     com = "LGU"
# else:
#     com = "알수없음"
# print(f"당신은 {com} 사용자입니다.")