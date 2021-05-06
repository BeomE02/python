marks = []

for i in range(5):
    scr = int(input("%d번 학생의 성적을 입력하시오 : " % (i+1)))
    marks.append(scr)

number = 0
sum = 0

for mark in marks:
    number = number + 1
    sum = sum + mark
    if mark >= 60:
        print("%d번 학생의 점수는 %d이고 합격입니다." % (number, mark))
    else:
        print("%d번 학생의 점수는 %d이고 불합격입니다." % (number, mark))

print("전체 학생의 총합 점수는 %d 이고 평균은 %.2f 입니다." % (sum,(sum/number)))
