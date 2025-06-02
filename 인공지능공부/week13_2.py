class People:
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        print(f"Hello, My name is {self.name}")

p1 = People("Hong")
p2 = People("Kim")

p1.sayHello() # 파이썬이 자동으로 객체를 호출
p2.sayHello() # 파이썬이 자동으로 객체를 호출
People.sayHello(p1) # 명시적으로 객체를 호출
People.sayHello(p2) # 명시적으로 객체를 호출
