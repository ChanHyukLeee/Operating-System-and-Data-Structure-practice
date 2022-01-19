"""
    root node is at data[1]
    parent of array i is at (i-1)/2
    left child of array i is at 2i+1
    right child of array i is at 2i+2
    data : array of data's key
    valuearray : array of data's value
    주의점 : 만약 넣는 key 값이 100이상이라면 valuearray의 size를 추가해야한다.
"""

class BST_Array():
    def __init__(self):
        # data에 None 값을 8개 삽입(index out of range 에러 방지)
        self.data = [None] * 8
        self.valuearray = [None] * 1000
    
    # size of data
    def __len__(self):
        return len(self.data)

    # 삽입할 숫자가 data의 사이즈를 넘으면 
    # data의 사이즈를 2배로 늘린다.
    def resize_array(self, size):
        for _ in range(size):
            self.data.append(None)
    
    # k 값 삽입
    def put(self,k, value):
        self.valuearray[k] = value 
        return self.put_item(1, k)
    
    def put_item(self, parent, k):
        # 사이즈가 부족하면 늘린다.
        if parent >= len(self.data):
            self.resize_array(parent)
        # 자리가 비어있다면 삽입
        if self.data[parent] == None:
            self.data[parent] = k
        else:
            # 오른쪽 서브트리 
            if k > self.data[parent]:
                parent = (2*parent) + 2
                return self.put_item(parent,k)
            # 왼쪽 서브트리
            elif k < self.data[parent]:
                parent = (2*parent) + 1
                return self.put_item(parent,k)
            # 동일하다면 중복값을 허용하지 않으므로 
            # 같은 값 자리에 삽입
            else:
                self.data[parent] = k
            
    # k값 찾기
    def get(self, k):
        return self.get_item(1, k)
    
    def get_item(self, i, k):
        if self.data[i] == None:
            return None
        # 오른쪽 서브트리 탐색
        if k > self.data[i]:
            i = (2*i) + 2
            return self.get_item(i, k)
        # 왼쪽 서브트리 탐색
        elif k < self.data[i]:
            i = (2*i) + 1
            return self.get_item(i,k)
        # 탐색 완료
        else:
            return self.valuearray[k]

    # check minimum value of BST
    def min(self):
        if self.data[1] == None:
            return None
        return self.minimum(1)
    
    def minimum(self, i):
        if (self.data[2*i+1] == None):
            return self.data[i]
        return self.minimum(2*i+1)
    
    # delete minimum value of BST 
    def delete_min(self):
        if self.data[1] == None:
            print('Tree is empty')
        return self.del_min(1)
    
    def del_min(self, i):
        if self.data[2*i+1] != None:
            return self.del_min(2*i + 1)
        temp = self.data[i]
        self.data[i] = None
        self.reorder(i)
        return temp
    
    # k값 delete
    def delete(self, k):
        return self._del(1, k)
    
    def _del(self, i, k):
        if self.data[i] == None:
            return None
        if k > self.data[i]:
            i = (2*i) + 2
            return self._del(i, k)
        elif k < self.data[i]:
            i = (2*i) + 1
            return self._del(i,k)
        else:
            temp = self.data[i]
            self.data[i] = None
            self.reorder(i)
            return temp

    # 지우고 나서 array BST에 맞게 재설정
    def reorder(self, i):
        # 만약에 구하는 값이 list index에서 벗어난다면
        # none값을 return한다.
        if 2*i+1 >= len(self.data):
            return None
        left = self.data[2*i + 1]
        right = self.data[2*i + 2]
        # case 1 : child가 없는 경우
        if left == None and right == None:
            self.data[i] = None
            return None
        # case 2 : child가 left만 있는 경우
        elif left != None and right == None:
            self.data[i] = left
            self.data[2*i + 1] = None
            return self.reorder(2*i + 1)
        # case 3 : child가 right만 있는 경우
        elif right != None and left == None:
            self.data[i] = right
            self.data[2*i + 2] = None
            return self.reorder(2*i + 2)
        # case 4 : child가 left, right 둘 다 있는 경우 
        else:
            # right subtree에서 가장 작은 경우를 제거할 노드에 위치시킴
            change_idx = self.find_smallest_right(2*i + 2)
            self.data[i] = self.data[change_idx]
            self.data[change_idx] = None
            return self.reorder(change_idx)
            
    # right subtree에서 가장 작은 경우
    # 가장 left node를 찾으면 됨
    def find_smallest_right(self, i):
        if self.data[2*i + 1] == None:
            return i
        else:
            return self.find_smallest_right(2*i + 1)

    #CLR순, HW(2-1)과 만드는 방식 동일
    def preorder(self):
        return self._preorder(1)

    def _preorder(self, i):
        value = self.data[i]
        left = self.data[2*i + 1]
        right = self.data[2*i + 2]
        if value != None:
            print(str(value), ' ', end=' ')
        if left != None:
            self._preorder(2*i+1)
        if right != None:
            self._preorder(2*i+2)

    #LRC순, Hw(2-1)과 만드는 방식 동일
    def postorder(self):
        return self._postorder(1)

    def _postorder(self,i):
        value = self.data[i]
        left = self.data[2*i + 1]
        right = self.data[2*i + 2]
        if left != None:
            self._postorder(2*i+1)
        if right != None:
            self._postorder(2*i+2)
        if value != None:
            print(str(value), ' ', end=' ')
        
    
    #LCR순, HW(2-1)과 만드는 방식 동일
    def inorder(self):
        return self._inorder(1)
    
    def _inorder(self, i):
        value = self.data[i]
        left = self.data[2*i + 1]
        right = self.data[2*i + 2]
        if left != None:
            self._inorder(2*i+1)
        if value != None:
            print(str(value), ' ', end=' ')
        if right != None:
            self._inorder(2*i+2)

    #level
    def levelorder(self):
        self._levelorder(1)
    
    """ 
    root node는 원래 level 0부터 시작이지만 편의를 위해 level 1부터 시작한다고 하자
    self.data에서 각 level에 해당하는 index는
        
        level 1 : 1
        level 2 : 3,4
        level 3 : 7,8,9,10
        level 4 : 15 - 22
        ... ...
    
    각 레벨의 처음 인덱스는 (2**level) - 1이고 인덱스의 개수는 2**(level - 1)이다. 
    이를 바탕으로 _levelorder를 만들었다.

    """
    
    def _levelorder(self, level):
        idx = (2**level) - 1
        num = 2**(level - 1)
        if idx + num -1 >= len(self.data):
            return None
        for i in range(num):
            if self.data[idx + i] != None:
                print(str(self.data[idx + i]), ' ', end=' ')
        return self._levelorder(level + 1)    


if __name__ == '__main__':
    print("\n_________ Question 2 ___________\n")
    bst_array = BST_Array()
    print("임의의 순서 10, 20, ... , 100 key 값 삽입 ")
    bst_array.put(50, 'a')
    bst_array.put(40, 'b')
    bst_array.put(60, 'c')
    bst_array.put(70, 'd')
    bst_array.put(20, 'e')
    bst_array.put(10, 'f')
    bst_array.put(30, 'g')
    bst_array.put(80, 'h')
    bst_array.put(90, 'i')
    bst_array.put(100, 'j')
    bst_array.order()
    print("입력 후 20, 50, 최솟값 제거")
    bst_array.delete(20)
    bst_array.delete(50)
    bst_array.delete_min()
    bst_array.order()
    print("\n30 값 찾기")
    print(bst_array.get(30), '\n')
    print("삭제된 10 값 찾기")
    print(bst_array.get(10), '\n')
    print("preorder : ", end = '')
    bst_array.preorder()
    print()
    print("postorder : ", end = '')
    bst_array.postorder()
    print()
    print("inorder : ", end = '')
    bst_array.inorder()
    print()
    print("levelorder : ", end = '')
    bst_array.levelorder()
