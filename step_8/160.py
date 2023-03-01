# 160
# 파일 이름이 저장된 리스트에서 확장자가 .h나 .c인 파일을 화면에 출력하라.

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# intra.c
# define.h

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for 변수 in 리스트:
    변수_split = 변수.split(".")
    if 변수_split[1] in ["c", "h"]:
        print(변수)

# 다른 답안:
# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# for 변수 in 리스트:
#   split = 변수.split(".")
#   if (split[1] == "h") or (split[1] == "c"):
#     print(변수)
