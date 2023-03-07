# 255 클래스 생성자-2
# 사람 (Human) 클래스에 (이름, 나이, 성별)을 받는 생성자를 추가하세요.

# >>> areum = Human("아름", 25, "여자")

class Human:
  def __init__(self, name, age, gender):
    self.name = name
    self.ager = age
    self.gender = gender

areum = Human("아름", 25, "여자")
print(areum.name)