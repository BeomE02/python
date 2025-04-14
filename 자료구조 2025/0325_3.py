a = int(input("수입력 : "))

if not isinstance(a, int) or a < 1 or a > 10:
    print("잘못된 입력")
elif a == 1:
    print("소수 아님")
elif a in [2, 3, 5, 7]:
    print("소수")
else:
    print("소수 아님")
