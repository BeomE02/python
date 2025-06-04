class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, second):
            return Vector(self.x + second.x, self.y + second.y)
    
    def __repr__(self):
         return f"Vector({self.x}, {self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"
    
def addVector(v1, v2):
     return Vector(v1.x + v2.x, v1.y + v2.y)
#================================================
class School:
     studentCount = 0
     students = []  #생성되는 학생들 저장.

     def __init__(self, name):
          self.name = name
          School.studentCount += 1
          School.students.append(self)

     def __repr__(self):
          return f"학생({self.name})"
    
     def showCount(self):
          print(f"이 학교에는 학생이 총 [{School.studentCount}]명 압니다.")

     def showAllName(self):
          for item in School.students:
               print(item)
#================================================

#================================================
s1 = School("홍길동")
s2 = School("이순신")
del s1
s2.showAllName()

s1 = School.students[0]
s1.showAllName()
