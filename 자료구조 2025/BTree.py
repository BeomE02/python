#===============================================================
# 이진 트리 (Binary Tree)
#===============================================================
from Queue import Queue
#===============================================================
class BTree:
    def __init__(self, value):
        self.key = value
        self.left = None    # 트로 노드 생성 초기에는 왼쪽, 오른쪽 자식 트리가 없으므로 None
        self.right = None
    
    #-----------------------------------------------------------
    def __str__(self):  # #"[100]"
        return f"[{self.key}]"
    #-----------------------------------------------------------
    # 노드를 포함한 왼쪽과 오른쪽 자식 노드의 상황까지 함께 표현하는 문자열을 반환하기
    def node(self): # print(NodeA), "[B]<-[A]->[C]", "[B]<-[A]->[None]"
        r = ""
        # 왼쪽 자식 노드 문자열 정리
        if self.left:
            r += str(self.left)
        else:
            r += "[None]"
        # 자신과 좌우 연결 화살표 정리
        r += "<-" + str(self) + "->"
        # 오른쪽 자식 노드 문자열 정리
        if self.right:
            r += str(self.right)
        else:
            r += "[None]"
        # 완성된 문자열 반환
        return r
    #-----------------------------------------------------------
    # 전위 순회 (Preorder traversal)
    # 1. root 방문 (방문 => 순회)
    # 2. 왼쪽 자식 트리를 같은 방식으로 방문.
    # 3. 오른쪽 자식 트리를 같은 방식으로 방문
    def preOrder(self):
        print(self, " ", end="")
        if self.left:
            self.left.preOrder()
        if self.right:
            self.right.preOrder()
    #-----------------------------------------------------------
    def inOrder(self):
        if self.left:
            self.left.inOrder()
        print(self, " ", end="")
        if self.right:
            self.right.inOrder()
    #-----------------------------------------------------------
    def postOrder(self):
        if self.left:
            self.left.postOrder()
        if self.right:
            self.right.postOrder()
        print(self, " ", end="")
    #-----------------------------------------------------------
    def levelOrder(self):
        queue = Queue() # 레벨 순회시 다음 방문할 노드들을 저장하고 저장된 순서대로 꺼내오기 위해
        queue.add(self)
        
        while not queue.isEmpty():
            node = queue.remove()
            print(node, " ", end="")
            if node.left:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)
        print("") # 출력 종료 후, 줄바꿈 처리용
#===============================================================
nodeA = BTree("A")
nodeB = BTree("B")
nodeC = BTree("C")

nodeA.left = nodeB
nodeA.right = nodeC
#-------------------
nodeA.preOrder()
print()
nodeA.inOrder()
print()
nodeA.postOrder()
print()
nodeA.levelOrder()
