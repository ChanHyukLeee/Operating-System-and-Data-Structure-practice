class Node:
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

"""
    key = BST에 들어갈 숫자
    value = key's name
    n = node
"""

class BST_Linked_Base:
    def __init__(self):
        # root of Tree
        self.root = None
    
    # 탐색
    def get(self,k):
        return self.get_item(self.root, k)
    
    def get_item(self, n, k):
        # 탐색 실패
        if n==None:
            return None
        # 왼쪽 서브트리 탐색
        if n.key > k:
            return self.get_item(n.left,k)
        # 오른쪽 서브트리 탐색
        elif n.key < k :
            return self.get_item(n.right,k)
        # key값 찾아서 탐색 성공
        else:
            return n.value  

    # 삽입
    def put(self, key, value):
        self.root = self.put_item(self.root, key, value)
    
    def put_item(self, n, key, value):
        # 노드 생성
        if n==None:
            return Node(key, value)
        # 왼쪽 서브트리 탐색
        if n.key > key:
            n.left = self.put_item(n.left, key, value)
        # 오른쪽 서브트리 탐색
        elif n.key< key:
            n.right = self.put_item(n.right, key, value)
        # key값 put
        else:
            n.value = value
        return n
    
    # 최솟값 찾기
    def min(self):
        if self.root==None:
            return None
        return self.minimum(self.root)
    
    def minimum(self,n):
        # 최솟값 가진 노드 출력
        if n.left == None:
            return n
        return self.minimum(n.left)
    
    # 최솟값 삭제
    def delete_min(self):
        if self.root==None:
            print("Tree is empty")
        self.root = self.del_min(self.root)
    
    def del_min(self, n):
        # 최솟값 삭제
        if n.left == None:
            return n.right
        n.left = self.del_min(n.left)
        return n
    
    # 특정 노드 제거
    def delete(self, k):
        self.root = self.del_node(self.root, k)
    
    def del_node(self, n, k):
        if n == None:
            return None
        # 왼쪽 서브트리 탐색
        if n.key > k:
            n.left = self.del_node(n.left, k)
        # 오른쪽 서브트리 탐색
        elif n.key< k:
            n.right = self.del_node(n.right, k)
        # 제거 대상 탐색완료
        else:
            if n.right == None:
                return n.left
            if n.left == None:
                return n.right
            # target : deleting node
            target = n
            n = self.minimum(target.right)
            n.right = self.del_min(target.right)
            n.left = target.left
        return n

    def preorder(self, n):
        if n!= None:
            print(str(n.key), ' ', end=' ')
            if n.left :
                self.preorder(n.left)
            if n.right:
                self.preorder(n.right)
    
    def postorder(self, n):
        if n!= None: 
            if n.left :
                self.postorder(n.left)
            if n.right:
                self.postorder(n.right)
            print(str(n.key), ' ', end=' ')

    def inorder(self, n):
        if n!= None: 
            if n.left :
                self.inorder(n.left)
            print(str(n.key), ' ', end=' ')
            if n.right:
                self.inorder(n.right)
            
    def levelorder(self, root):
        q = []
        q.append(root)
        while len(q) != 0:
            t= q.pop(0)
            print(str(t.key), ' ', end=' ')
            if t.left != None:
                q.append(t.left)
            if t.right != None:
                q.append(t.right)




if __name__ == '__main__':
    print("\n_________ Question 1 ___________\n")
    bst_ll = BST_Linked_Base()
    print("임의의 순서 10, 20, ... , 100 key 값 삽입 ")
    bst_ll.put(50, 'a')
    bst_ll.put(40, 'b')
    bst_ll.put(60, 'c')
    bst_ll.put(70, 'd')
    bst_ll.put(20, 'e')
    bst_ll.put(10, 'f')
    bst_ll.put(30, 'g')
    bst_ll.put(80, 'h')
    bst_ll.put(90, 'i')
    bst_ll.put(100, 'j')
    print("입력 후 20, 50, 최솟값 제거")
    bst_ll.delete(20)
    bst_ll.delete(50)
    bst_ll.delete_min()
    print("\n30 값 찾기")
    print(bst_ll.get(30), '\n')
    print("삭제된 10 값 찾기")
    print(bst_ll.get(10), '\n')
    print("preorder : ", end = '')
    bst_ll.preorder(bst_ll.root)
    print()
    print("postorder : ", end = '')
    bst_ll.postorder(bst_ll.root)
    print()
    print("inorder : ", end = '')
    bst_ll.inorder(bst_ll.root)
    print()
    print("levelorder : ", end = '')
    bst_ll.levelorder(bst_ll.root)
    print()
