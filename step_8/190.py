# 190
# 리스트에 저장된 데이터를 아래와 같이 출력하라.

# apart = [[101, 102], [201, 202], [301, 302]]
# 101 호
# 102 호
# 201 호
# 202 호
# 301 호
# 302 호
# -----

apart = [[101, 102], [201, 202], [301, 302]]

for row in apart: 
  for col in row:
    print(col, "호")
print("-----")

