# 159
# 파일 이름이 저장된 리스트에서 확장자가 .h인 파일 이름을 출력하라.

# 리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']
# intra.h
# define.h

리스트 = ['intra.h', 'intra.c', 'define.h', 'run.py']

for 변수 in 리스트:
    변수_split = 변수.split(".")
    if 변수_split[1] == "h":
        print(변수)
