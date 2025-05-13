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
        if targetNode is None:
            self.append(value)
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
        else:
            newNode = Node(value)
            newNode.next = targetNode.next
            newNode.prev = targetNode
            targetNode.next.prev = newNode
            targetNode.next = newNode
            self.count += 1
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
    #-------------------------------------------------------
#===========================================================
dlist = DList()
dlist.append(100)
dlist.showList()
dlist.append(200)
dlist.showList()
dlist.append(300)
dlist.insertBefore(dlist.find(200), 50)
dlist.showList()
