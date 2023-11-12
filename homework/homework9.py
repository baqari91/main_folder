from random import randint
li = []
c = 0
while c<=9:
    li.append(randint(-1000,1000))
    c+=1
li.sort()
print(li)


from random import randint
li = []
c = 0
while c<=9:
    li.append(randint(-1000,1000))
    c+=1
result = sorted(li, reverse=True)
print(result)

from time import time

def show_time(func):
    start_time = time()
    func()
    end_time = time()
    print(end_time-start_time)

@show_time
def bubble_sort():
    arr=[]
    for  num in range(0,1000):
        arr.append(randint(0,100))
    n = len(arr)-1
    sorted2 = False
    while not sorted2:
        sorted2 = True
        for i in range(0,n):
            if arr[i] > arr[i+1]:
                sorted2 = False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    print("bubble sort 1000 elements:", end=" ")

@show_time
def selection_sort():
    arr=[]
    for  num in range(0,1000):
        arr.append(randint(0,100))
    indexing_lenghth=range(0,len(arr)-1)
    for i in indexing_lenghth:
        min_value = i
        for k in range(i+1,len(arr)):
            if arr[k]<arr[min_value]:
                min_value=k
        if min_value!=i:
            arr[min_value],arr[i]=arr[i],arr[min_value]
    print("selection sort 1000 elements: ", end=" ")



@show_time
def bubble_sort():
    arr=[]
    for  num in range(0,2000):
        arr.append(randint(0,100))
    n = len(arr)-1
    sorted2 = False
    while not sorted2:
        sorted2 = True
        for i in range(0,n):
            if arr[i] > arr[i+1]:
                sorted2 = False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    print("bubble sort 2000 elements:", end=" ")
    
@show_time
def selection_sort():
    arr=[]
    for  num in range(0,2000):
        arr.append(randint(0,100))
    indexing_lenghth=range(0,len(arr)-1)
    for i in indexing_lenghth:
        min_value = i
        for k in range(i+1,len(arr)):
            if arr[k]<arr[min_value]:
                min_value=k
        if min_value!=i:
            arr[min_value],arr[i]=arr[i],arr[min_value]
    print("selection sort 2000 elements: ", end=" ")


@show_time
def bubble_sort():
    arr=[]
    for  num in range(0,3000):
        arr.append(randint(0,100))
    n = len(arr)-1
    sorted2 = False
    while not sorted2:
        sorted2 = True
        for i in range(0,n):
            if arr[i] > arr[i+1]:
                sorted2 = False
                arr[i],arr[i+1]=arr[i+1],arr[i]
    print("bubble sort 3000 elements:", end=" ")


@show_time
def selection_sort():
    arr=[]
    for  num in range(0,3000):
        arr.append(randint(0,100))
    indexing_lenghth=range(0,len(arr)-1)
    for i in indexing_lenghth:
        min_value = i
        for k in range(i+1,len(arr)):
            if arr[k]<arr[min_value]:
                min_value=k
        if min_value!=i:
            arr[min_value],arr[i]=arr[i],arr[min_value]
    print("selection sort 3000 elements: ", end=" ")
    
  