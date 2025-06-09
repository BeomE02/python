#=======================================================
# 이중 연결 리스트를 이용하여 스택(Staxk) 구현하기
#=======================================================
from DList import *
#=======================================================
class StackUnderflow(Exception):
    pass

class Stack(DList):
    # 스택에 새 데이터를 추가하는 연산
    def push(self, value):
        self.insertFront(value)

    # 스택에 맨 위에 데이터를 가져오는 연산 (맨 위의 데이터는 스택에서 제거됨)
    def pop(self):
        if self.isEmpty():
            raise StackUnderflow("Stack Empty!!")
        else:
            returnValue = self.head.data
            self.remove(self.head)
            return returnValue 

    # 스택이 비었는지 확인하는 연산 (반환 값: True : 빈스택, False : 데이터가 있음.)
    def isEmpty(self):
        if self.count == 0:
            return True
        return False

    # 스택에서 top 항목의 값을 읽어오는 연산 (읽은 항목이 제거되지 않음. pop() 비교)
    def peek(self):
        if self.isEmpty():
            raise StackUnderflow("Stack Empty!!")
        return self.head.data

#=================================================================================

# 괄호 매칭이 순서대로 되었는지를 확인하는 함수
# 사용 가능한 괄호 : (), {}, [], <> 예: "{()<<>>[[]]}"
# 반환값: True: 매칭이 잘 되었을 경우, False: 매칭에 문제가 발생했을 경우.
# 매칭에 문제가 생긴 괄호를 출력한다

# def checkParentheses(parens):
#     stack = Stack()
#     match = {')': '(', '}': '{', ']': '[', '>': '<'}

#     for c in parens:
#         if c in "({[<":
#             stack.push(c)
#         elif c in ")}]>":
#             if stack.isEmpty():
#                 return f"여는 괄호 없이 닫는 괄호 '{c}'가 등장함"
#             top = stack.pop()
#             if match[c] != top:
#                 return f"괄호 짝이 맞지 않음: 열림 '{top}' - 닫힘 '{c}'"

#     if not stack.isEmpty():
#        return f"닫히지 않은 괄호가 남아 있음: {stack.items}"

#     return True

def checkParenthese(st):

    print(f"{st} : ", end="")

    pleft = "([{<"
    pright = ")]}>"
    pairs = "(){}[]<>"

    stack = Stack()

    for item in st:
        if item in pleft:
            stack.push(item)
        elif item in pright:
            top = stack.pop()
            if (top + item) in pairs:
                continue
            else:
                print(f"매칭 오류 발생{top}, {item}")
                return False
        else:
            continue
    if not stack.isEmpty():
        print("닫히지 않은 괄호가 남아있습니다.")
        return False
    else:
        return True

#=================================================================================
