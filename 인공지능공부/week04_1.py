"""
list comprehension 연습
"""

lst = [2, 3, 4, 5, 3, 12, 34, 60]
#lst에서 홀수만 찾아서 만든 새 리스트 생성하기
"""
result = [] #홀수만 담을 빈 리스트 생성

for item in lst:
    if item%2 > 0:
        result.append(item) # result 홀수 추가

print(lst)
print(result)
"""

"""
result = [item for item in lst if item%2 > 0]

print(lst)
print(result)
"""
c = ["korea", "Japan", "Jameica", "Ukraine", "South Africa", "United States of America"]

fristName = [item[0] for item in c]
print(fristName)

resulf = [item[len(c)] for item in c]
print(resulf)
