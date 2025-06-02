import time

def apply_discount(price, dc=10):
    return price - price * float(f"0.{dc}")
#===================================================
def total_avg(*args):
    s = sum(args)
    return s, s/len(args)
#=================================================== 
def join_strings(*args):
    result = ""
    for item in args:
        result += item
    return result
#===================================================
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result
#===================================================
#재귀 함수(recursive function)
def fact(n):
    if n==1:
        return 1
    return n * fact(n-1)
#===================================================
# n = 900
# start = time.time()
# f = factorial(n)
# finish = time.time()
# interval = finish - start
# print(f"반복문 팩토리얼 : {interval}")
# print("%20s: %.10f"%("반복문 함수 : ", interval))
# #===================================================
# n = 900
# start = time.time()
# f = fact(n)
# finish = time.time()
# interval = finish - start
# print(f"재귀함수 팩토리얼 : {interval}")
# print("%20s: %.10f"%("재귀함수 : ", interval))
# #===================================================
# 숫자들로 채워진 리스트를 넘겨받아 합계를 계산하여 반환한다. (단, 재귀함수로 구현하기)

def sumList(lst):
    if len(lst) == 0:
        return lst[0]
    else:
        return lst[0] + sumList(lst[1:])
    

print(sumList([10, 20, 30, 40, 50]))

#===================================================
