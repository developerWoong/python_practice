# 169
# 1~10까지의 숫자 중 모든 홀수의 합을 출력하는 프로그램을 for 문을 사용하여 작성하라.

# 합: 25
sum = 0
for i in range(1, 11, 2):
  sum = sum + i 

print("합 :", sum)