print ('done')

grade_dict = {}

class Student:
  def __init__(self, name, grade ):
    self.name = name
    self.grade = grade
    grade_dict[self.name]= self.grade #otomatis add ke dict klo di init


shiro = Student('shironeko', 97)
dan = Student('daniel', 85)

print(shiro.name + ' ' + str(shiro.grade))

print(grade_dict)