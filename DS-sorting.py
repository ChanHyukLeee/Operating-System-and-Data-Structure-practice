# Running time comparison of sorting
import time
from numpy.random import randint
import matplotlib.pyplot as plt

# selection sort
# arr: list to sort
def selection_sort(arr):
    for i in range(0, len(arr)-1):
        minimum = i
        for j in range(i, len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        # minimum value는 앞으로        
        arr[i], arr[minimum] = arr[minimum], arr[i]
    return arr

# bubble sort
# arr : list to sort
def bubble_sort(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if arr[j] > arr[j+1]:
                # swap
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr
                
# quick sort 
# arr: list to sort

def quick_sort(arr):
    if len(arr) <=1:
        return arr
    # pivot을 array의 중간에 설정
    pivot = arr[len(arr)//2]
    # Array 분리
    lesser_arr, equal_arr, greater_arr=[],[],[]
    for num in arr:
        if num<pivot:
            lesser_arr.append(num)
        elif num>pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr)+ equal_arr + quick_sort(greater_arr)

# quick sort의 worst case
# pivot을 맨 처음 값을 선정했다. 
def worst_quick_sort(arr):
    if len(arr) <=1:
        return arr
    # pivot을 array에 처음으로 설정
    pivot = arr[0]
    # Array 분리
    lesser_arr, equal_arr, greater_arr=[],[],[]
    for num in arr:
        if num<pivot:
            lesser_arr.append(num)
        elif num>pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr)+ equal_arr + quick_sort(greater_arr)

# Merge sort
# arr: list to sort
def merge_sort(arr):
    if len(arr) > 1:
  
        # Finding the mid of the array
        mid = len(arr)//2
        
        # left array
        L = arr[:mid]
        # right array
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)
  
        i = j = k = 0

        # data를 copy
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # element 남은게 있나 확인
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

# radix sort
# arr: list to sort
# exp : 자릿수, 여기서는 10진수 활용
def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while int(max1/exp)>0:
        counting_sort(arr, exp)
        exp*=10
    return arr

# counting sort, radix sort's subroutine
def counting_sort(arr, exp):
    n = len(arr)
    max = 9
    count = [0]*(max+1)
    output = [-1]*n
    for i in arr:
        index = int((i/exp)%10)
        count[index] += 1
    
    for i in range(max):
        count[i+1] += count[i]
    
    i = n-1
    while i>=0:
        temp = arr[i]
        index = int((arr[i]/exp)%10)
        count[index] -=1
        position = count[index]
        output[position] = temp
        i -=1
        
    for i in range(0,n):
        arr[i] = output[i]


# find running time when best case
# Already sorted array case
def best_case_time():
    elements = list()
    times = list()
    for i in range(1, 10):
        a = []

        # best case array
        for j in range(100000*i):
            a.append(j)

        start = time.time()
        
        # 원하는 모델을 돌려서 확인한다. 
        # selection_sort(a)
        # bubble_sort(a)
        # quick_sort(a)
        merge_sort(a)
        
        end = time.time()

        print(len(a), "elements time complexity : ", end-start)
        elements.append(len(a))
        times.append(end-start)
        
    plt.title('Best case')
    plt.xlabel('List Length')
    plt.ylabel('Running Time')
    # 모델 이름을 바꾼다
    plt.plot(elements, times, label ='Merge Sort')
    plt.grid()
    plt.legend()
    plt.show()

# radix sort의 best case
def best_case_radixsort():
    elements = list()
    times = list()
    for i in range(1, 10):
        a = []

        # best case array
        for j in range(100000*i):
            a.append(100000 + j)

        start = time.time()
        
        radix_sort(a)
        
        end = time.time()

        print(len(a), "elements time complexity : ", end-start)
        elements.append(len(a))
        times.append(end-start)
        
    plt.title('Best case')
    plt.xlabel('List Length')
    plt.ylabel('Running Time')
    plt.plot(elements, times, label ='Radix Sort')
    plt.grid()
    plt.legend()
    plt.show()
    

# find running time when average case
# random array case
def average_case_time():
    elements = list()
    times = list()
    for i in range(1, 10):
 
    # Average case : Random array
        a = randint(0, 100000 * i, 100000 * i)
        randint()
        start = time.time()
        
        # 원하는 모델을 돌려서 확인한다. 
        # selection_sort(a)
        # bubble_sort(a)
        # quick_sort(a)
        # merge_sort(a)
        radix_sort(a)
        
        end = time.time()
    
        print(len(a), "elements time complexity :", end-start)
        elements.append(len(a))
        times.append(end-start)
    
    plt.title('Average case')
    plt.xlabel('List Length')
    plt.ylabel('Running Time')
    # sort 이름 바꾸기
    plt.plot(elements, times, label ='Radix sort')
    plt.grid()
    plt.legend()
    plt.show()

# find running time when worst case
# 
# def worst_case_time(n):
def worst_case_time():
    elements = list()
    times = list()
    for i in range(1, 10):
        a = []

        # worst case array
        for j in range(100000*i):
            a.append((100000*i)-j)

        start = time.time()
        
        # 원하는 모델을 돌려서 확인한다. 
        # selection_sort(a)
        # bubble_sort(a)
        # worst_quick_sort(a)
        merge_sort(a)
        
        end = time.time()

        print(len(a), "elements time complexity : ", end-start)
        elements.append(len(a))
        times.append(end-start)
    
    plt.title('Worst case')
    plt.xlabel('List Length')
    plt.ylabel('Running Time')
    # 모델 이름을 바꾼다
    plt.plot(elements, times, label ='Merge Sort')
    plt.grid()
    plt.legend()
    plt.show()    

# radix sort의 worst case
def worst_case_radixsort():
    elements = list()
    times = list()
    for i in range(1, 10):
        a = []

        # worst case array

        for j in range(100000*i):
            a.append(100000 + j)
        a.append(1000000000000)

        start = time.time()
        
        radix_sort(a)
        
        end = time.time()

        print(len(a), "elements time complexity : ", end-start)
        elements.append(len(a))
        times.append(end-start)
        
    plt.title('Worst case')
    plt.xlabel('List Length')
    plt.ylabel('Running Time')
    plt.plot(elements, times, label ='Radix Sort')
    plt.grid()
    plt.legend()
    plt.show()

if __name__ == "__main__":
    
    # 측정하고 싶은 sorting 알고리즘을 
    # best_case_time(), average_case_time(), worst_case_time() 함수 내부에
    # 교채해서 진행했다.
    
    print()
    best_case_time()
    print()
    average_case_time()
    print()
    worst_case_time()