# Exception 정의
class EmptyError(Exception):
    pass

# Stack based by Array
# 참고 코드와 달리 class를 이용해서 Array기반 Stack을 구현함
class ArrayStack:
    def __init__(self):
        self._data = [] # Stack Array 생성
    
    # 스택의 사이즈
    def __len__(self):
        return len(self._data)
    
    # 스택이 비어있다면 True 아니면 False
    def is_empty(self):
        return len(self._data) == 0
    
    # 스택에 item push 하기
    def push(self, item):
        self._data.append(item)
    
    # 스택에 맨 끝 항목 제거 및 반환
    def pop(self):
        if (len(self._data) != 0):
            item = self._data.pop(-1)
            return item
        else:
            raise EmptyError('Underflow')
    
    # 스택에 맨 끝 항목 조회
    def peek(self):
        if (len(self._data) != 0):
            return self._data[-1]
        else:
            raise EmptyError('Underflow')
    
    # 스택 문자열 표현
    def __repr__(self):
        return repr(self._data) 

# Node class
class Node:
    def __init__(self, item, link):
        self.item = item # element
        self.link = link # link to the next node

# 단순연결리스트로 구현한 스택
class LLStack:
    def __init__(self):
        self.head = None
        self.size = 0

    # 스택이 비어있다면 True 아니면 False
    def is_empty(self):
        return self.size == 0
    
    # 스택의 사이즈
    def __len__(self):
        return self.size
    
    # 스택에 item push 하기
    def push(self, item):
        self.head = Node(item, self.head)
        self.size += 1

    # 스택에 맨 끝 항목 제거 및 반환
    def pop(self):
        if (self.size != 0) :
            node = self.head
            self.head = node.link
            self.size -= 1
            return node.item
        else:
            raise EmptyError("UnderFlow")

    # 스택에 맨 끝 항목 조회
    def peek(self):
        if (self.size != 0) :
            return self.head.item
        else:
            raise EmptyError("UnderFlow")
    
    # 스택 출력
    def print_list(self):
        if self.is_empty():
            print("리스트 비어있음")
        else:
            print('rear : ', end ='')
            p = self.head # head 다음부터 
            while p != None: # tail 되기 전까지
                if p.link != None:
                    print(p.item, '-> ' , end = '')
                else:
                    print(p.item, end = '')
                p = p.link # 노드를 차례로 선택
            print(' : front')

# Array 기반 stack이 pop할때 
# element 개수에 따른 실행시간 반환 
def find_pop_ArrayStack(n):
    start_time = time.time()
    for _ in range(n):
        Array_stack.pop()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Array 기반 stack의 pop 수행시간 : ", elapsed_time)

# 연결리스트 기반 stack이 pop할때 
# element 개수에 따른 실행시간 반환 
def find_pop_LLStack(n):
    start_time = time.time()
    for _ in range(n):
        LL_stack.pop()
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("LinkedList 기반 stack의 pop 수행시간 : ", elapsed_time)

# Array 기반 stack이 push할때 
# element 개수에 따른 실행시간 반환 
def find_push_ArrayStack(n):
    start_time = time.time()
    for i in range(n):
        Array_stack.push(i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("Array 기반 stack의 push 수행시간 : ", elapsed_time)

# 연결리스트 기반 stack이 push할때 
# element 개수에 따른 실행시간 반환 
def find_push_LLStack(n):
    start_time = time.time()
    for i in range(n):
        LL_stack.push(i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print("LinkedList 기반 stack의 push 수행시간 : ", elapsed_time)


if __name__ == '__main__':
    import time # 실행 시간 계산 위한 모듈

    Array_stack = ArrayStack()
    print("------------- 문제 2-1 -------------")
    print("스택이 비었나요? : ", Array_stack.is_empty())

    print("스택에 0-4를 대입하겠습니다.")
    for i in range(5):
        Array_stack.push(i)
    print("스택의 크기는 :", len(Array_stack))
    print("스택은 다음과 같습니다.")
    print(Array_stack)

    print("스택의 맨 끝 값 제거 및 반환(pop) : ", end = '')
    print(Array_stack.pop())
    print(Array_stack)
    print("이 때 스택의 사이즈는 :", len(Array_stack))

    print("스택에 맨 끝 항목을 조회 (top) :", end='')
    print(Array_stack.peek())
    print("이 때 반환된 값은 삭제되지 않는다.")
    print(Array_stack)

    print("10이라는 숫자를 맨 끝에 삽입합시다.")
    Array_stack.push(10)
    print(Array_stack)


    print(" ")

    LL_stack = LLStack()
    print("------------- 문제 2-2 -------------")
    print("스택이 비었나요? : ", LL_stack.is_empty())

    print("스택에 0-4를 대입하겠습니다.")
    for i in range(5):
        LL_stack.push(i)
    print("스택의 크기는 :", len(LL_stack))
    print("스택은 다음과 같습니다.")
    LL_stack.print_list()

    print("스택의 맨 끝 값 제거 및 반환(pop) : ", end ='')
    print(LL_stack.pop())
    LL_stack.print_list()
    print("이 때 스택의 사이즈는 :", len(LL_stack))

    print("스택에 맨 끝 항목을 조회 (top) :", end='')
    print(LL_stack.peek())
    print("이 때 반환된 값은 삭제되지 않는다.")
    LL_stack.print_list()

    print("10이라는 숫자를 맨 끝에 삽입합시다.")
    LL_stack.push(10)
    LL_stack.print_list()

    print(" ")
    print("------------- 문제 2-3 -------------")
    #초기화
    for i in range(5):
        Array_stack.pop()
        LL_stack.pop()
    print("time 모듈을 이용하여 running time을 비교하겠다. ")
    print("1) element 10,000개의 push 수행시간을 비교")
    find_push_ArrayStack(10000)
    find_push_LLStack(10000)
    print("element 10,000개의 pop 수행시간을 비교")
    find_pop_ArrayStack(10000)
    find_pop_LLStack(10000)

    print("2) element 1,000,000개 의 push 수행시간을 비교")
    find_push_ArrayStack(1000000)
    find_push_LLStack(1000000)
    print("element 1,000,000개의 pop 수행시간을 비교")
    find_pop_ArrayStack(1000000)
    find_pop_LLStack(1000000)

    print("3) element 10,000,000개 의 push 수행시간을 비교")
    find_push_ArrayStack(10000000)
    find_push_LLStack(10000000)
    print("element 10,000,000개의 pop 수행시간을 비교")
    find_pop_ArrayStack(10000000)
    find_pop_LLStack(10000000)

    print("3) element 100,000,000개 의 push 수행시간을 비교")
    find_push_ArrayStack(100000000)
    find_push_LLStack(100000000)
    print("element 100,000,000개의 pop 수행시간을 비교")
    find_pop_ArrayStack(100000000)
    find_pop_LLStack(100000000)
         
