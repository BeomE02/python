class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    #객체를 문자열로 표현하여 반환.
    def __str__(self):
        return f"{self.name}({self.age})"

    def intro(self):
        print(f"안녕하세요 저는 {self.age}세 {self.name}입니다.")

#==========================================
#객체 생성

p = Person("홍길동", 20)
p.intro()

print(p)
