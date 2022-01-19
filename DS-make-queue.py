# Exception 정의
class EmptyError(Exception):
    pass

# array기반 queue
class Array_q:
    # array 생성
    def __init__(self):
        self.data = []

    # 큐가 비어있다면 True 아니면 False
    def isEmpty(self):
        return len(self.data) == 0

    # 큐의 사이즈
    def __len__(self):
        return len(self.data)
    
    # 큐에 맨 뒤에 삽입
    def add(self, item):
        self.data.append(item)
    
    # 큐의 맨 앞의 항목 삭제
    def remove(self):
        if (self.data != 0):
            item = self.data.pop(0)
            return item
        else:
            raise EmptyError('UnderFlow')
    
    # 큐 출력
    def print_q(self):
        print('front ->', end='')
        for i in range(len(self.data)):
            print('{!s:<8}'.format(self.data[i]), end ='')
        print(' <- rear')

# Node class
class Node:
    def __init__(self, item, link):
        self.item = item # element
        self.link = link # link to the next node

class LL_q:
    def __init__(self):
            self.head = None
            self.tail = None
            self.count = 0

    # 스택이 비어있다면 True 아니면 False
    def isEmpty(self):
        return self.count == 0
    
    # 큐의 사이즈
    def __len__(self):
        return self.count

    # 큐에 맨 뒤에 삽입
    def add(self, item):
        # 새 노드 형성
        node = Node(item, None)
        # head가 없다면
        if not self.head:
            #head와 tail을 node로 지정
            self.head = node
            self.tail = node
        else:
            #tail 뒤에 노드 지정
            self.tail.next = node
            self.tail = node
        self.count += 1
    
     # 큐의 맨 앞의 항목 삭제
    def remove(self):
        # 사이즈가 0이 아니라면
        if self.count != 0:
            # head 제거
            head_item = self.head.item
            self.head = self.head.next
            self.count -= 1
            return head_item
        else:
            raise EmptyError('UnderFlow')      

    # 큐 출력
    def print_q(self):
        if self.isEmpty():
            print("리스트 비어있음")
        else:
            print('front : ', end ='')
            p = self.head # head 다음부터 
            while p != self.tail: # tail 되기 전까지
                print(p.item, '-> ' , end = '')
                p = p.next # 노드를 차례로 선택
            print(p.item, end = '')
            print(' : rear')
    
# Array 기반 queue가 add할때 
# element 개수에 따른 실행시간 반환 
def find_add_ArrayQueue(n):
    start_time = time.time()
    for i in range(n):
        array_q.add(i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Array 기반 queue의 add 수행시간 : ", elapsed_time)

# 연결리스트 기반 queue가 pop할때 
# element 개수에 따른 실행시간 반환 
def find_add_LLQueue(n):
    start_time = time.time()
    for i in range(n):
        linked_q.add(i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("LinkedList 기반 queue의 add 수행시간 : ", elapsed_time)

# Array 기반 queue가 remove할때 
# element 개수에 따른 실행시간 반환 
def find_remove_ArrayQueue(n):
    start_time = time.time()
    for _ in range(n):
        array_q.remove()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Array 기반 queue의 remove 수행시간 : ", elapsed_time)

# 연결리스트 기반 queue가 remove할때 
# element 개수에 따른 실행시간 반환 
def find_remove_LLQueue(n):
    start_time = time.time()
    for _ in range(n):
        linked_q.remove()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("LinkedList 기반 queue의 remove 수행시간 : ", elapsed_time)

if __name__ == "__main__":
    
    import time # 실행 시간 계산 위한 모듈

    print("------------- 문제 3-1 -------------")
    array_q = Array_q()
    print("큐가 비었나요? : ", array_q.isEmpty())

    print("큐에 0-4를 대입하겠습니다.")
    for i in range(5):
        array_q.add(i)
    print("큐의 크기는 :", len(array_q))
    print("큐는 다음과 같습니다.")
    array_q.print_q()

    print("큐의 맨 앞 값 제거 및 반환(remove) : ", end = '')
    print(array_q.remove())
    array_q.print_q()
    print("이 때 스택의 사이즈는 :", len(array_q))

    print("10이라는 숫자를 맨 끝에 삽입합시다.")
    array_q.add(10)
    array_q.print_q()

    print("")
    print("------------- 문제 3-2 -------------")
    linked_q = LL_q()
    print("큐가 비었나요? : ", linked_q.isEmpty())

    print("큐에 0-4를 대입하겠습니다.")
    for i in range(5):
        linked_q.add(i)
    print("큐의 크기는 :", len(linked_q))
    print("큐는 다음과 같습니다.")
    linked_q.print_q()

    print("큐의 맨 앞 값 제거 및 반환(remove) : ", end = '')
    print(linked_q.remove())
    linked_q.print_q()
    print("이 때 스택의 사이즈는 :", len(linked_q))

    print("10이라는 숫자를 맨 끝에 삽입합시다.")
    linked_q.add(10)
    linked_q.print_q()

    print(" ")
    print("------------- 문제 3-3 -------------")
    # 초기화
    for _ in range(4):
        array_q.remove()
        linked_q.remove()
    
    print("time 모듈을 이용하여 running time을 비교하겠다. ")
    print("1) element 10,000개의 add 수행시간을 비교")
    find_add_ArrayQueue(10000)
    find_add_LLQueue(10000)
    print("element 10,000개의 remove 수행시간을 비교")
    find_remove_ArrayQueue(10000)
    find_remove_LLQueue(10000)
    print(" ")

    print("2) element 100,000개의 add 수행시간을 비교")
    find_add_ArrayQueue(100000)
    find_add_LLQueue(100000)
    print("element 1,000,000개의 remove 수행시간을 비교")
    find_remove_ArrayQueue(100000)
    find_remove_LLQueue(100000)
    print(" ")

    print("3) element 1,000,000개의 add 수행시간을 비교")
    find_add_ArrayQueue(1000000)
    find_add_LLQueue(1000000)
    print("element 1,000,000개의 remove 수행시간을 비교")
    find_remove_ArrayQueue(1000000)
    find_remove_LLQueue(1000000)

    print("extra_work : element 10,000,000 add 수행시간비교")
    find_add_ArrayQueue(10000000)
    find_add_LLQueue(10000000)