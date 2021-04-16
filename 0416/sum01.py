"""
print("하재범")
print("202106019")
print("하재범", end="")
print("202106019")
"""


uum = int(input("정수입력 : "))
sum = 0
for i in range (1,(num+1)):
    if i < num:
        print(i,"+", end="")
    else:
        print(i,"+",end="")
    sum += i
        
print(sum)

