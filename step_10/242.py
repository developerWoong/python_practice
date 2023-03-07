# 242 현재시간의 타입
# datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.

import datetime

now = datetime.datetime.now()
print(now, type(now))