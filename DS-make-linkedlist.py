# Exception 정의
class EmptyError(Exception):
    pass

# Singly linked list
class SList:
    # 노드 생성
    class Node:
        def __init__(self, item, link): 
            self.item = item # element
            self.next = link # link to the next node
    
    # singly linkedlist 생성
    def __init__(self):
        self.head = None
        self.size = 0
    
    # 리스트 사이즈
    def Size(self): 
        return self.size

    # 리스트가 비어있는지 여부
    def is_empty(self): 
        return self.size==0

    # 맨 앞에 새 노드 삽입
    def insert_front(self, item):
        if self.is_empty():
            self.head = self.Node(item, None) # 새 노드 참조
        else:
            self.head = self.Node(item, self.head) # 새 노드 참조
        self.size += 1
    
    # p가 가리키는 노드 이후에 새 노드 삽입
    def insert_after(self, item, p):
        p.next = SList.Node(item, p.next) # 새 노드가 p 다음 노드 됨
        self.size += 1
    
    #p가 가리키는 노드의 앞 노드 삭제
    def delete_front(self):
        if self.is_empty():
            # 링크드리스트가 비어있을 때 에러 발생
            raise EmptyError('Underflow')
        else:
            self.head = self.head.next
            self.size -= 1

    # p가 가리키는 노드의 뒷 노드 삭제
    def delete_after(self, p):
        if self.is_empty():
            # 링크드리스트가 비어있을 때 에러 발생
            raise EmptyError('Underflow')
        t = p.next
        p.next = t.next
        self.size -= 1
    
    # target이 가리키는 노드 탐색
    def search(self, target):
        p = self.head
        for k in range(self. size):
            if target == p.item:
                return k # 탐색값
            p = p.next
        return None #탐색값 없음
    
    def print_list(self):
        p = self.head
        while p: 
            if p.next != None:
                print(p.item, '-> ', end = '')
            else:
                print(p.item)
            p = p.next

# Doubly Linked List
class DList:
    # 노드 생성
    class Node:
        def __init__(self, item, prev, link): 
            self.item = item # element
            self.prev = prev # link to the previous node
            self.next = link # link to the next node
    
    # Doubly linked list 생성
    def __init__(self):
        #head와 tail에 Dummy node 생성, 서로 연결만 해준다
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0

    # 연결리스트 사이즈    
    def Size(self):
        return self.size
    
    # 연결리스트 비어있는지 여부
    def is_empty(self):
        return self.size == 0
    
    # 새 노드를 p 앞에 삽입
    def insert_before(self, p, item):
        t = p.prev # 노드에 들어갈 t 정의
        n = self.Node(item, t, p) # n이 새 노드 참조
        p.prev = n # 뒤 노드와 새 노드 연결
        t.next = n # 잎 노드와 새 노드 연결
        self.size += 1 # 사이즈 증가
    
    # 새 노드를 p 뒤에 삽입
    def insert_after(self, p, item):
        t = p.next # 노드에 들어갈 t 정의
        n = self.Node(item, p, t) # n이 새 노드 참조
        t.prev = n # 앞 노드와 새 노드 연결
        p.next = n # 뒤 노드와 새 노드 연결
        self.size += 1
    
    # 노드 x 삭제
    # x는 가비지 컬렉션에 의해 처리 및 링크드리스트 연결 분리
    def delete(self, x):
        if self.is_empty(): # 아무것도 없다면
            raise EmptyError('Underflow')
        else:
            f = x.prev # f는 x의 전 노드
            r = x.next # r은 x의 다음 노드
            # x를 제외하고 앞뒤 노드를 서로 연결
            f.next = r 
            r.prev = f 
            self.size -= 1
            return x.item
    
    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            p = self.head.next # head 다음부터 
            while p != self.tail: # tail 되기 전까지
                if p.next != self.tail:
                    print(p.item, ' <=> ' , end = '')
                else:
                    print(p.item)
                p = p.next # 노드를 차례로 선택


if __name__ == '__main__':

    print("------- 문제 1-1 -------")
    singly_ll = SList()
    print("연결리스트가 비었나요? : ", singly_ll.is_empty())

    print("0, 1, 2, 3, 4를 연결리스트에 삽입")
    for i in range(5):
        singly_ll.insert_front(i)  
    print("연결리스트 출력:")
    singly_ll.print_list()

    print("첫 노드 삭제 : ")
    singly_ll.delete_front()
    singly_ll.print_list()

    print ("맨 앞에 새 노드 10 삽입 : " )
    singly_ll.insert_front(10)
    singly_ll.print_list()

    print("10 뒤에 새 노드 9 삽입 : ")
    singly_ll.insert_after(9, singly_ll.head)
    singly_ll.print_list()

    print("9 뒤에 노드 삭제 : ")
    singly_ll.delete_after(singly_ll.head.next)
    singly_ll.print_list()

    print("10을 찾아보기")
    print(singly_ll.search(10), "번째") # 0번째 위치
    print("1을 찾아보기")
    print(singly_ll.search(1), "번째") # 3번째 위치

    print("연결리스트 갯수 : ")
    print(singly_ll.Size())

    print(" ")
    print("------- 문제 1-2 -------")
    Double_ll = DList()
    print("연결리스트가 비었나요? : ", Double_ll.is_empty())

    print("0, 1, 2, 3을 연결리스트에 삽입")
    # insert_after 이용
    Double_ll.insert_after(Double_ll.head, 0)
    Double_ll.insert_after(Double_ll.head.next, 1)

    # insert_before 이용
    Double_ll.insert_before(Double_ll.tail, 3)
    Double_ll.insert_before(Double_ll.tail.prev, 2)

    print("연결리스트 출력 : ")
    Double_ll.print_list()

    print("2 뒤에 노드 삭제 : ")
    Double_ll.delete(Double_ll.tail.prev)
    Double_ll.print_list()
    
    print("첫 노드 삭제 : ")
    Double_ll.delete(Double_ll.head.next)
    Double_ll.print_list()

    print("연결리스트 사이즈 : ")
    print(Double_ll.Size())