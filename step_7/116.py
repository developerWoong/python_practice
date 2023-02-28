# 116
# 사용자로부터 입력 받은 시간이 정각인지 판별하라.

# >> 현재시간: 02: 00
# 정각 입니다.
# >> 현재시간: 03: 10
# 정각이 아닙니다

current_time = input("현재시간: ").split(":")
if int(current_time[1]) == 00 : 
    print("정각입니다.")
elif int(current_time[1]) != 00 : 
    print("정각이 아닙니다.")

# 다른 답변:
# time = input("현재시간: ")
# if time[-2:] == "00":
#     print("정각 입니다.")
# else:
#     print("정각이 아닙니다.")
