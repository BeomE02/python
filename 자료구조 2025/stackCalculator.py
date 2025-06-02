from Queue import *
from Stack import *
#=======================================================
# Infix 수식 문자열을 읽어 token(연산자, 피연산자, 괄호) 단위로 분리하여 순서대로 queue에 저장하고
# queue를 반환한다.
# 예 : "23.4 * (43.4 + 35) / 23.1243" => ["23.4", "*", "(", "43.4", "+", "35", ")", "/", "23.1243"]
def toTokens(strInfix):
    chList = list(strInfix) # 입력 문자열(strInFix)을 문자 단위로 쪼개서 list로 만든다.
    ops = "+-*/()"
    nums = "0123456789."
    numToken = ""  # nums에 포함되는 문자열 토큰 분리를 위한 임시 버퍼
    tokenList = [] # 토큰이 하나씩 분리될 때마다 차례대로 저장할 리스트

    while chList:               # chList가 비어있지 않으면,
        ch = chList.pop(0)      #chList에서 앞에서 하나씩 차례대로 꺼내와서 처리한다.
        if ch in ops:           # 현재 문자가 연산자이거나 괄호 문자이면
            tokenList.append(ch) # 토큰으로 분리된 문자이므로 tokenList에 저장한다.
        elif ch in nums:        # 숫자(실수형 포함)을 표현하는 문자이면
            numToken += ch      # 우선, 현재 문자를 numToken에 저장하고
            while chList:       # 수 토큰 분리를 위한 반복문 시작, (읽을 항목이 chList에 남아 있으면 반복한다.)
                if chList[0] in nums: # chList의 남은 항목들 중의 첫 항목이 숫자로 포함될 수 있는 문자이면
                    numToken += chList.pop(0) # chList에서 첫 항목을 꺼내서 numToken에 이어 붙인다.
                else:            # 숫자로 연결될 수 있는 문자가 아니면,
                    break        # 숫자 토큰 읽기를 중단하고
            tokenList.append(float(numToken)) # 수로 분리된 토큰(numToken)은 수(float)로 변환하여 저장한다.
            numToken = ""       # 다음 숫자 토큰 분리를 위해 초기화 한다.
        else:   # 빈 칸 등 수식과 무관한 문자항목은 무시하고 다음 항목으로 반복 계속.
            continue
    # 토큰 분리가 마무리 되었으므로 결과 반환
    return tokenList

# infix 토큰 리스트를 postfix 토큰 queue로 반환한다.
def infix2postfix(lstInfix):    # Infix 수식 문자열을 토큰으로 분리하여 저장한 list를 매개변수 받는다.
    stack = Stack() # 변환 작업용 stack
    queue = Queue() # 출력용 queue
    ops = "+-*/"
    priority = {"*":3, "/":3, "+":2, "-":2, "(":1, ")":1}
    
    while lstInfix: # 토큰 리스트에 토큰이 남아 있으면 계속한다.
        token = lstInfix.pop(0) # 리스트의 맨 앞에 있는 항목을 꺼내 온다.
        # 1. 토큰이 피연산자이면 출력한다.
        if type(token) == float:
            queue.add(token)
        # 2. 왼쪽 괄호이면, push
        elif token == "(":
            stack.push(token)
        # 3. 오른쪽 괄호이면, 왼쪽 괄호가 나올때까지 pop하면 출력. 단, 오른쪽아너 왼쪽 괄호는 출력하지 않음
        elif token == ")":
            while stack.peek() != "(":
                queue.add(stack.pop())
            stack.pop() # 스택에서 나타난 왼쪽 괄호는 버린다.
        # 4. 연산자이면, 자신의 우선순위보다 낮은 연산자가 스택 top에 나타날 때까지 pop하여 출력하고 읽은 연산자를 push
        else:
            pass

def StackCalculator(queuePostfix):
    pass

#=======================================================
l = toTokens("23.4 * (43.4 + 35) / 23.1243")
print(l)
