# 163
# 1부터 30까지의 숫자 중 3의 배수를 출력하라.

# 3
# 6
# 9
# 12
# 15
# 18
# 21
# 24
# 27
# 30

for  i in range(1, 31):
  if i % 3 == 0 : 
    print(i)

# 다른 답안:
# for num in range(3, 31, 3):
#     print(num)
