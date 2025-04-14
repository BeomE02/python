#함수 정의 연습

#-----------------------------------------------------

def printHello():
    print("Hello World")

#-----------------------------------------------------
    
def sayHello(name = "익명자"):
    print(f"안녕하세요 {name}씨, 반갑습니다.")
    
#-----------------------------------------------------

def intro(age, name="홍길동"):
    print(f"저는 {age}세, {name}입니다.")

    
#-----------------------------------------------------

def myFruits(*fruits): # 호출 시 전달되는 인수들은 list에 담겨 fruits에 전달된다.
    for item in fruits:
        print(f"I like {item}.")
        
#-----------------------------------------------------

def average(*avg):
    
    """
    total = 0
    for item in avg:
        total += item
    result = total / len(avg)
    print(result)
    """
    
    print(sum(avg)/len(avg))

#-----------------------------------------------------

def avg(a, b):
    return (a+b)/2

#-----------------------------------------------------

def calc(a, b):
    return (a+b, a-b, a*b, a/b)

#-----------------------------------------------------

# 함수 호출 영역

print(avg(3,4))
