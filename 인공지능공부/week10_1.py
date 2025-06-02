"""
함수 문서화 연습
"""

def greet(name="홍길동"):
    """
    넘겨받은 이름의 사람에 인사말을 다음과 같이 출력한다.
    name: 인사를 받을 사람의 이름
    출력: 안녕하세요 홍길동님
    return: None
    """
    print(f"안녕하세요 {name}님")
#=======================================================================
def htmlCode(tag, text, className):
    """
    HTML 코드를 생성하여 출력한다.
    매개변수:
        Tag: HTML Tag Name
        text: Tag에 포함될 내용 <Tag>text...</Tag>
        className: class 속성값.
    반환값: 없음.
    """
    print(f"<{tag} class='{className}'>{text}</{tag}>")
#=======================================================================
def averageAll(*args):
    """
    매개 변수로 전달된 값들의 평균을 계산하여 반환한다.
    매개 변수: 임의의 개수의 수(number)
    반환값: 평균값
    """
    return sum(args)/len(args)
#=======================================================================
def dispInfo(**kargs):
    """
    매개변수명과 매개변수의 값이 자유롭게 지정되며 전달가능한 형식의 함수
    함수 호출 시 전달한 매개변수명과 매개변수값은 dictionary로 저장되어 전달된다.
    """
    for key, value in kargs.items():
        print(f"{key}:[{value}]")
#=======================================================================
def area(**kargs):
    """
    매개변수 (키워드 인자):
    - width: 너비
    - height: 높이
    - radius: 반지름

    조건:
    - width, height 모두 있으면: 직사각형 (width * height)
    - width만 있으면: 정사각형 (width * width)
    - radius만 있으면: 원 (3.14 * radius^2)
    - 그 외의 조합은 ValueError 발생
    """ 
    try:
        if 'radius' in kargs:
            if 'width' in kargs or 'height' in kargs:
                raise ValueError("radius랑 width/height를 같이 사용할 수 없어.")
            print(3.14 * kargs['radius'] * kargs['radius'])
            return
        if 'width' in kargs and 'height' in kargs:
            print(kargs['width'] * kargs['height'])
            return
        if 'width' in kargs and 'height' not in kargs:
            print(kargs['width'] * kargs['width'])
            return
        raise ValueError(f"매개변수 오류 {kargs}")
    except ValueError as e:
        print(e)

#=======================================================================
area(width=100, height=200) # width x height
area(radius=10) #3.14*10*10
area(width=10) # 10 x 10 (정사각형)
area(radius=10, height=10) #오류
area(r=10, w=20) #오류