class Test:
    def __init__(self, value1, value2):
        self.a = value1
        self.b = value2

t = Test(10, 20)
t2 = Test(100, 200)
del t2.a
t.c = 100 # 객체 생성된 이후에도 해당 객체에 속성을 추가할 수 있다. (다른 객체에 적용되지 않음)

print(f"t.a = {t.a}, t.b = {t.b} t.c = {t.c}")
print(f"t.b = {t2.b}")