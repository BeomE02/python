#input으로 입력한 데이터는 모두 문자열입니다. 
year = input("오늘의 년도를 입력하시오 : ")
month = input("오늘의 월을 입력하시오 : ")
day = input("오늘의 일을 입력하시오 : ")
print("오늘은 "+year+"년 "+month+"월 "+day+"일입니다.")

#입력한 문자열을 정수로 바꾸는 함수는 int입니다.
year = int(input("오늘의 년도를 입력하시오 : "))
month = int(input("오늘의 월을 입력하시오 : "))
day = int(input("오늘의 일을 입력하시오 : "))
print("오늘은 "+str(year)+"년 "+str(month)+"월 "+str(day)+"일입니다.")
#+는 문자열과 문자열을 결합, str함수를 이용하여 정수를 문자열로 변환
#정수를 문자열로 바꾸는 함수는 str입니다.

print("오늘은 ",year,"년 ",month,"월 ",day,"일입니다.")
#print에서 문자열과 정수를 출력하는 방법 중에 하나는 ,를 이용하면 됩니다
