class Test:
    def __init__(self, value1, value2):
        self.a = value1
        self.b = value2

    def __str__(self):
        return f"({self.a}.{self.b})"

t = Test(10, 20)
t2 = Test(100, 200)
print(t, t2)
