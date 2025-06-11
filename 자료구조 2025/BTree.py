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
    #-----------------------------------------------------------
    # 주어진 이진 트리의 노드 수를 카운팅하여 반환. (재귀함수 활용하기)
    # 왼쪽 자식 트리의 개수 + 오른쪽 자식 트리의 개수 + 1 (자신)
    def nodeCount(self):
        if self.left:
            leftCount = self.left.nodeCount()
        else:
            leftCount = 0
        if self.right:
            rightCount = self.right.nodeCount()
        else:
            rightCount = 0
        return 1 + leftCount + rightCount
    
    def nodeCount2(self):
        count = 1 # self 자신 먼저 카운팅
        if self.left:
            count += self.left.nodeCount2()
        if self.right:
            count += self.right.nodeCount2()
        return count
    #-----------------------------------------------------------
    # 트리의 높이(height)를 계산하여 반환하기. (재귀함수 활용하기)
    def height(self):
        if self.left:
            leftHeight = self.left.height()
        else:
            leftHeight = 0
        if self.right:
            rightHeight = self.right.height()
        else:
            rightHeight = 0
        return 1 + max(leftHeight, rightHeight)
    
    def height2(self):
        if self.left is None and self.right is None:
            return 1
        if self.left is None:
            return 1 + self.right.height2()
        if self.right is None:
            return 1 + self.left.height2()
        return 1 + max(self.left.height2(), self.right.height2())
    #-----------------------------------------------------------
    # 완전 이진 트리(complete binary tree)여부를 확인하여 True/False 값을 반환
    # 반복문과 Queue 사용하여 구현
    def isComplete(self):
        queue = Queue()
        queue.add(self)
        danger = False # 이후에 자식이 없는 노드가 발견되면 True 설정 예정.

        while not queue.isEmpty():
            node = queue.remove()
            if node.left:
                if danger: # 현재 노드(node) 이전에 자식이 없었던(왼쪽, 오른쪽 무관) 노드가 발생했었는지를 확인.
                    return False
                queue.add(node.left)
            else:
                danger = True

            if node.right:
                if danger: # 현재 노드(node) 이전에 자식이 없었던(왼쪽, 오른쪽 무관) 노드가 발생했었는지를 확인.
                    return False
                queue.add(node.right)
            else:
                danger = True

        # queue의 모든 노드들을 다 방문하고 여기까지 오면 완전 이진 트리
        return True  
    #-----------------------------------------------------------
    # 완전 이진 트리를 리스트(배열)로 변환하기
    def toList(self):
        if not self.isComplete():
            return None
        lst = [None]
        queue = Queue()
        queue.add(self)
        while not queue.isEmpty():
            node = queue.remove()
            lst.append(node.key)
            if node.left:
                queue.add(node.left)
            if node.right:
                queue.add(node.right)
        return lst
    #-----------------------------------------------------------
#===============================================================
class BSTree(BTree):
    # 이진 탐색 트리에 새 키값을 가진 노드를 추가한다.
    # 같은 값이 있을 때는 노드를 추가하지 않는다.
    def insert(self, value):
        if value < self.key:
            if self.left:
                return self.left.insert(value)
            else:
                self.left = BSTree(value)
                return 1
        elif value > self.key:
            if self.right:
                return self.right.insert(value)
            else:
                self.right = BSTree(value)
                return 1
        else:
            return 0
#===============================================================
node = BSTree(100)
node.insert(50)
node.insert(500)
node.insert(130)
node.insert(60)
node.insert(55)
node.insert(20)
node.insert(150)
node.insert(250)
node.insert(80)
node.insert(10)

node.inOrder()
#-------------------
#nodeA = BTree("A")
#nodeB = BTree("B")
#nodeC = BTree("C")
#nodeD = BTree("D")
#nodeE = BTree("E")
#nodeF = BTree("F")
#nodeG = BTree("G")
#nodeH = BTree("H")
#nodeI = BTree("I")
#nodeA.left = nodeB
#nodeA.right = nodeC
#nodeB.left = nodeD
#nodeB.right = nodeE
#nodeC.right = nodeF
#nodeD.right = nodeG
#nodeE.left = nodeH
#nodeD.left = nodeI
