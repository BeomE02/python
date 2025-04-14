#===================================================
# 단순 연결 리스트 (Singly Linked List)
#===================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f"[{self.data}]"
#===================================================
class SList:
    def __init__(self):
        self.head = None        #SList의 첫 노드를 가르킨다. (초기값은 빈 리스트이므로 None)
        self.count = 0          #SList에 연결된 노드의 개수(를 항상 유지한다.)
    #-----------------------------------------------
    def __len__(self):
        return self.count
    #-----------------------------------------------
    #기존의 리스트 맨 앞에 새 노드(newNode)를 연결한다.
    def insertFront(self, newNode):
        if self.head is None:
            self.head = newNode
            self.count = 1
        else: #한개 이상의 노드가 있는 경우
            newNode.next = self.head
            self.head = newNode
            self.count += 1
    #-----------------------------------------------
    #기존의 리스트 맨 뒤에 새 노드(newNode)를 연결한다.
    def append(self, newNode):
        if self.head is None:   # SList가 빈 리스트인 경우
            self.head = newNode # 추가하려는 새 노드(newNode)가 첫 노드가 된다.
            self.count = 1
        else:                   # 한개 이상의 노드가 있는 경우, (마지막 노드를 찾아서 그 뒤에 newNode를 연결한다.)
            current = self.head # 리스트의 첫 노드(self.head)부터 순서대로 확인하며 마지막 노드를 찾는다.
            while current.next is not None: # 현재 노드(current)의 다음 노드가 있으면
                current = current.next      # current는 다음 노드를 가르키도록 설정한다.
            # current.next가 None이면 while 종료, ==> current가 마지막 노드임을 의미
            # 새 노드(newNode)를 current 뒤에 연결한다.
            current.next = newNode
            # 새 노드가 추가 되었으므로 self.count 값 변경
            self.count += 1
    #-----------------------------------------------
    # 리스트의 현재 연결 상황을 출력한다.
    # 빈 리스트의 경우 : [Empty]
    # 그 외의 경우 : [100]-[200]-...-[300]-[None] 형식으로 출력 예정
    def showList(self):
        print("[head]->", end="")   # 초기 정보를 출력하고 줄바꿈 하지 않음. (-> 다음 이어질 출력과 연결)
        current = self.head         # 리스트의 첫 노드부터 차례대로 방문하며 노드 값을 출력하기

        while current is not None:
            print(f"{current}->", end="") # 현재 노드(current)의 data 출력.
            current = current.next              # 현재 노드의 위치를 다음 노드로 이동
        
        print(f"||({self.count} nodes.)")
    #-----------------------------------------------
    def appendValue(self, Value):
        self.append(Node(Value))
    #-----------------------------------------------
    # 리스트의 첫 노드(head)를 삭제하며 반환한다. (빈 리스트이면 None 반환)
    def unshift(self):
        if self.head is None:
            return None
        else:
           header = self.head
           self.head = self.head.next
           header.next = None
           self.count -= 1
           return header
    #-----------------------------------------------
    # 리스트의 노드 연결 순서를 역순으로 재구성한다. (헤드가 마지막 노드로 변경된다.)
    def reverse(self):
        if self.head is None:
            return None
        else:
            previous = None
            current = self.head
            while current is not None:
                next_node = current.next     # 다음 노드 저장
                current.next = previous      # 현재 노드의 방향을 이전 노드로 바꿈
                previous = current           # previous를 현재 노드로 이동
                current = next_node          # current를 다음 노드로 이동
            self.head = previous             # 마지막 노드가 새로운 head가 됨

    def reverse2(self):
        revList = SList() # 역순으로 재구성하는게 활용할 빈 리스트 생성.

        # 기존 리스트의 첫 노드를 차례대로 제거하며 revList에 insertFront() 처리한다.
        while self.head is not None:
            h = self.unshift() # 기존 리스트의 첫 노드를 제거한다. (h에 저장)
            revList.insertFront(h) # 새 리스트(revList)의 insertFront(로) 제거한 노드를 추가한다.

        # 역순으로 재구성된 리스트의 정보를 현재 리스트로 옮겨온다.
        self.head = revList.head
        self.count = revList.count

    #-----------------------------------------------
    # 리스트의 정렬 상태를 유지하면서 새 노드를 추가한다.
    def insertSorted(self, newNode):
        if self.head is None:
            self.head = newNode
            self.count = 1
        elif newNode.data < self.head.data:
            # head보다 작으면 맨 앞에 삽입
            newNode.next = self.head
            self.head = newNode
            self.count += 1
        else:
            current = self.head
            # newNode가 들어갈 위치 바로 앞을 찾는다
            while current.next is not None and current.next.data < newNode.data:
                current = current.next

            # 중간 또는 마지막 위치에 삽입
            newNode.next = current.next
            current.next = newNode
            self.count += 1
            
    #-----------------------------------------------
    # 특정값을 가진 노드를 연결 리스트에서 제거한다.
    # 반환값 : 제거한 노드를 반환, 없으면 None

    def remove(self, value):
        current = self.head
        previous = None

        while current is not None:
            if current.data == value:
                if previous is None:
                    # 삭제할 노드가 맨 앞에 있는 경우
                    self.head = current.next
                else:
                    # 삭제할 노드가 중간 또는 끝에 있는 경우
                    previous.next = current.next
                self.count -= 1
                return current  # 삭제한 노드를 반환
            previous = current
            current = current.next
        return None  # 삭제할 노드를 찾지 못한 경우


    def remove2(self, value):
    # head가 삭제 대상이면 바로 처리
        if self.head is not None and self.head.data == value:
            removed = self.head
            self.head = self.head.next
            self.count -= 1
            return removed

        current = self.head
        # current는 삭제 대상의 바로 앞 노드
        while current is not None and current.next is not None:
            if current.next.data == value:
                removed = current.next
                current.next = current.next.next
                self.count -= 1
                return removed
            current = current.next

        return None  # 못 찾은 경우
    
    def remove3(self, value):
        targetNode = self.find(value)
        if targetNode is None:
            return None
        else:
            previous = None         # current를 바로 이어서 따라가는 역할, 최종 삭제 작업에서 중요한 역할.
            current = self.head
            while current is not targetNode:
                previous = current
                current = current.next
            
            # 이 지점에서는 current가 targetNode를 확인한 경우
            if previous is None:            #targetNode가 리스트의 첫 노드이므로
                self.head = current.next    #리스트의 첫 노드(head)는 targetNode의 다음 노드가 된다.
            else:
                previous.next = current.next 
            # 마무리 하고 반환값 설정
            current.next = None # 삭제 대상 노드의 연결 고리(next) 제거
            self.count -= 1
            return current
    #-----------------------------------------------
    # 특정값이 리스트에 포함되어 있는지 결과를 알려주기
    # 반환값 : 없을 경우 None, 있으면 해당 노드 반환
    def find(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            else:
                current = current.next
        # value를 찾지 못하면 None 반환
        return None

#===================================================

lst = SList()   #빈 리스트 하나 생성.
lst.insertSorted(Node(100))
lst.insertSorted(Node(200))
lst.insertSorted(Node(300))
lst.insertSorted(Node(300))
lst.insertSorted(Node(400))
lst.insertSorted(Node(100))
lst.insertSorted(Node(150))
lst.showList()
#===================================================
