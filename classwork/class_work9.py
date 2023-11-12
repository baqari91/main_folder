from random import randint

def list_generator(length):
    generated_list=[]
    for _ in range(0,length):
        generated_list.append(randint(1,1000))
    return generated_list

def instertion_sort():
    arr=list_generator(100)
    index_lenght=range(1,len(arr))
    for i in index_lenght:
        value_2sort=arr[i]
        while arr[i-1] > value_2sort and i > 0:
            arr[i],arr[i-1]=arr[i-1],arr[i]
            i=i-1
    print("insertion sort")
    return arr
print(instertion_sort())




from random import randint

 

def list_generator(length):

    generated_list=[]

    for _ in range(0,length):

        generated_list.append(randint(1,1000))

    return generated_list

 

my_list = list_generator(10)
def quick_sort(arr):
    length = len(arr)
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    items_greater = []
    items_lower = []
    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)
print(my_list)
print(quick_sort(my_list))


a =[1,3,10,15,20]

def binary_search(arr, element):
    begin_index = 0
    end_index = len(arr)-1
    while begin_index <= end_index:
        middle_point = begin_index+(end_index-begin_index)//2
        middle_point_value = arr[middle_point]
        if middle_point_value == element:
            return middle_point
        elif element < middle_point_value:
            end_index = middle_point-1
        else:
            begin_index = middle_point+1
    return None
print(a)
#მუშაობს დასორტირებულ სიებზე
print(binary_search(a, 10))


a = [1,5,12,3,22,6]
def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1
print(linear_search(a,27))