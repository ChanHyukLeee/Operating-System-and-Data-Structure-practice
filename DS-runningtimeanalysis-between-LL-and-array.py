import time
from DS-make-BST-in-Linkedlist import BST_Linked_Base
from DS-make-BST-in-array import BST_Array

# Array 기반 BST가 insert할때 
# node 개수에 따른 실행시간 반환 
def insert_ArrayBST(n):
    start_time = time.time()
    for i in range(n):
        BST_array.put(i,'a')
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_time = elapsed_time/n
    print("Array 기반 BST의 insert 전체시간 : ", elapsed_time)
    print("Array 기반 BST의 insert 평균시간 : ", avg_time)

# Linked List 기반 BST가 insert할때 
# node 개수에 따른 실행시간 반환 
def insert_LinkedBST(n):
    start_time = time.time()
    for i in range(n):
        BST_linked_base.put(i,'a')
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_time = elapsed_time/n
    print("LL 기반 BST의 insert 전체시간 : ", elapsed_time)
    print("LL 기반 BST의 insert 평균시간 : ", avg_time)

# Array 기반 BST를 search할때 
# 걸리는 시간
def find_ArrayBST(n):
    start_time = time.time()
    BST_array.get(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_time = elapsed_time/n
    print("Array 기반 BST의 search 전체시간 : ", elapsed_time)
    print("Array 기반 BST의 search 평균시간 : ", avg_time)

# Linked List 기반 BST를 search할때
# 걸리는 시간
def find_LinkedBST(n):
    start_time = time.time()
    BST_linked_base.get(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_time = elapsed_time/n
    print("LL 기반 BST의 search 전체시간 : ", elapsed_time)
    print("LL 기반 BST의 search 평균시간 : ", avg_time)

# Array 기반 BST가 minimum value를 remove할때 
# node 개수에 따른 실행시간 반환 
def delete_ArrayBST(n):
    start_time = time.time()
    for _ in range(n):
        BST_array.delete_min()
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_time = elapsed_time/n
    print("Array 기반 BST의 delete 전체시간 : ", elapsed_time)
    print("Array 기반 BST의 delete 평균시간 : ", avg_time)

# Linked List 기반 BST가 insert할때 
# node 개수에 따른 실행시간 반환 
def delete_LinkedBST(n):
    start_time = time.time()
    for _ in range(n):
        BST_linked_base.delete_min()
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_time = elapsed_time/n
    print("LL 기반 BST의 delete 전체시간 : ", elapsed_time)
    print("LL 기반 BST의 delete 평균시간 : ", avg_time)

if __name__ == '__main__':
    BST_array = BST_Array()
    BST_linked_base = BST_Linked_Base()
    print()
    print("______________________Question 3__________________")
    print()
    print("20개 삽입")
    print("______________________insert 평균시간__________________")
    print()
    insert_LinkedBST(20)
    insert_ArrayBST(20)
    print()
    print("______________________find 평균시간__________________")
    find_LinkedBST(19)
    find_ArrayBST(19)
    print()
    print("______________________delete 평균시간__________________")
    delete_LinkedBST(20)
    delete_ArrayBST(20)
    print()

    print("28개 삽입")
    print("______________________insert 평균시간__________________")
    print()
    insert_LinkedBST(28)
    insert_ArrayBST(28)
    print()
    print("______________________find 평균시간__________________")
    find_LinkedBST(27)
    find_ArrayBST(27)
    print()
    print("______________________delete 평균시간__________________")
    delete_LinkedBST(28)
    delete_ArrayBST(28)
    print()
    print("Linked list만 950개 삽입")
    print("______________________insert 평균시간__________________")
    print()
    insert_LinkedBST(950)
    print()
    print("______________________find 평균시간__________________")
    find_LinkedBST(949)
    print()
    print("______________________delete 평균시간__________________")
    delete_LinkedBST(950)

    insert_LinkedBST(950)
    print("다른 삭제방법")
    start_time = time.time()
    for i in range(950):
        BST_linked_base.delete(949-i)
    end_time = time.time()
    elapsed_time = end_time - start_time
    avg_time = elapsed_time / 950
    print("LL 기반 BST의 delete 전체시간 : ", elapsed_time)
    print("LL 기반 BST의 delete 평균시간 : ", avg_time)