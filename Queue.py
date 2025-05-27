#=======================================================
# 이중 연결 리스트를 이용하여 큐(queue) 구현하기
#=======================================================
from DList import *
#=======================================================
class QueueUnderflow(Exception):
    pass

class Queue(DList):
    # 큐에 새 데이터(value)를 추가한다.
    def add(self, value):
        self.append(value)

    #---------------------------------------------------
    # 큐에서 맨 앞(가장 오래 전에 추가된 데이터)에 있는 데이터를 꺼낸다.
    def remove(self):
        if self.isEmpty():
            raise QueueUnderflow("Queue Empty!!")
        else:
            returnValue = self.head.data
            super().remove(self.head)
            return returnValue 
#=======================================================
# Infix 수식 문자열을 읽어 token(연산자, 피연산자, 괄호) 단위로 분리하여 순서대로 queue에 저장하고
# queue를 반환한다.
# 예 : "23.4 * (43.4 + 35) / 23.1243" => ["23.4", "*"", "(", "43.4", "+"", "35", ")", "/", "23.1243"]
def toTokens(strInfix):
    queue = Queue()
    lst = []
    lst.append(token)
    queue.add(token)
    pass

def infix2postfix(lst, queue):
    pass
    
#=======================================================
queue = Queue()
queue.add(100)
queue.add(200)
queue.showList()
print(queue.remove())
queue.showList()
queue.remove()
queue.remove()
