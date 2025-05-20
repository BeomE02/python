"""
    이중 연결 리스트 (Double Linked List) 
"""
#===========================================================
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return f"[{self.data}]"
#===========================================================
class DList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    #-------------------------------------------------------
    def append(self, value):
        # 새로 추가할 노드 생성
        newNode = Node(value)
        # 빈 리스트인 경우를 먼저 확인하고 처리한다.
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:   # 빈 리스트가 아닌 경우에는 리스트의 tail이 가리키는 노드 뒤에 새 노드를 연결한다.
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        # 리스트의 노드 개수 증가 반영
        self.count += 1
    #-------------------------------------------------------
    def insertFront(self, value):
        newNode = Node(value)
        if self.count == 0: # 빈 리스트인 경우
            self.append(value)
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            self.count += 1
    #-------------------------------------------------------
    # 리스트에서 value값을 가진 첫 노드를 찾아서 반환한다.
    # 없으면 None 반환.
    def find(self, value):
        current = self.head
        while current is not None:
            if current.data == value:
                return current
            else:
                current = current.next
        return None
    #-------------------------------------------------------
    # 리스트의 존재하는 targetNode 앞에 value값을 가진 새 노드를 생성하여 삽입한다.
    def insertBefore(self, targetNode, value):
        if targetNode is None:
            return
        if targetNode is self.head:
            self.insertFront(value)
        else:
            newNode = Node(value)
            newNode.next = targetNode
            newNode.prev = targetNode.prev
            targetNode.prev.next = newNode
            targetNode.prev = newNode
            self.count += 1
    #-------------------------------------------------------
    def insertAfter(self, targetNode, value):
        if targetNode is None:
            return
        if targetNode is self.tail:
            self.append(value)
        else:
            newNode = Node(value)
            newNode.next = targetNode.next
            newNode.prev = targetNode
            targetNode.next.prev = newNode
            targetNode.next = newNode
            self.count += 1
    #-------------------------------------------------------
    # 현재 리스트(정렬되어 있는 것으로 간주) 상태를 유지하면서 새 값(value)를 가진 노드를 추가한다.
    # 같은 값을 가진 노드가 이미 있으면 그 노드 앞에 추가한다.
    # 반환값 없음.
    def insertSorted(self, value):
    #2. 노드가 1개 이상인 경우
    #   value보다 크거나 같은 값을 찾아 그 앞에 Node(Value)를 삽입한다.
        current = self.head
        while current is not None:
            if current.data >= value:
                self.insertBefore(current, value)
                return
            else:
                current = current.next
        #빈 리스트이거나 추가하려는 값이 기존 모든 노드들의 값보다 큰 경우 다음 코드가 실행된다.
        self.append(value)
    #-------------------------------------------------------
    # 리스트에서 지정된 노드(targetNode)를 삭제한다. (연결구조에서 배제한다.)
    # 반환값: 없음.
    def remove(self, targetNode):
        if targetNode is None:
            return
        if self.count == 1:
            self.head = None
            self.tail = None
        elif self.head is targetNode:
            self.head = targetNode.next
            targetNode.next.prev = None
        elif self.tail is targetNode:
            self.tail = targetNode.prev
            targetNode.prev.next = None
        else:
            targetNode.next.prev = targetNode.prev
            targetNode.prev.next = targetNode.next
        self.count -= 1
        del targetNode
    #-------------------------------------------------------
    def showList(self):
        print("[head]->", end="")
        # head부터 마지막 노드까지 차례대로 노드를 출력한다.
        current = self.head
        while current is not None:
            print(current, end="-")
            current = current.next
        #리스트의 노드 개수를 출력하면서 리스트 출력 마무리.
        print(f"({self.count} nodes.)")
    #-------------------------------------------------------
#===========================================================
dlist = DList()
dlist.insertSorted(50)
dlist.insertSorted(150)
dlist.insertSorted(30)
dlist.insertSorted(250)
dlist.insertSorted(100)
dlist.showList()
dlist.remove(dlist.find(150))
dlist.showList()
