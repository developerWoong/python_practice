# 227
# 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.

# printmxn("아이엠어보이유알어걸", 3)
# 아이엠
# 어보이
# 유알어
# 걸

def print_mxn(str, num):
    chunk_num = int(len(str)/num)
    for i in range(chunk_num + 1):
        print(str[i * num:i * num + num])
    