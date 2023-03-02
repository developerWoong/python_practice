# 194
# 191번 문제의 결괏값을 result 이름의 리스트에 2차원 배열로 저장하라. 저장 포맷은 아래와 같다. 각 행에 대한 데이터끼리 리스트에 저장되어야 한다.

# >> print(result)
# [
#     [2000.28, 3050.427, 2050.2870000000003, 1980.2772],
#     [7501.05, 2050.2870000000003, 2050.2870000000003, 1980.2772],
#     [15452.163, 15052.107, 15552.177, 14902.086000000001]
# ]

data = [
    [2000,  3050,  2050,  1980],
    [7500,  2050,  2050,  1980],
    [15450, 15050, 15550, 14900]
]

result = []
for line in data:
    sub = []
    for column in line:
        sub.append(column * 1.00014)
    result.append(sub)
print(result)
